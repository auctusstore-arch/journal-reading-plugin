#!/usr/bin/env python3
"""Hitung ulang ukuran efek dari angka mentah paper. Jangan pakai angka efek dari AI tanpa cek ini.

Dikotomus (2x2), event & total per kelompok:
  uv run python3 effect_calc.py binary --ee 12 --ne 150 --ce 27 --nc 150 [--harm]
    ee/ne = event/total intervensi, ce/nc = event/total kontrol.
    Output: EER, CER, RR, RRR, OR, ARR (atau ARI bila --harm / intervensi lebih buruk), NNT/NNH, 95% CI.

Diagnostik:
  uv run python3 effect_calc.py diag --tp 90 --fp 30 --fn 10 --tn 170
    Output: sensitivitas, spesifisitas, PPV, NPV, LR+, LR-, prevalensi, dengan 95% CI (Wilson).

Kontinu (selisih rerata, dua kelompok independen):
  uv run python3 effect_calc.py mean --m1 5.2 --sd1 1.1 --n1 60 --m2 6.0 --sd2 1.3 --n2 58
    Output: MD dengan 95% CI dan SMD (Hedges g).

Semua angka dibulatkan; tulis di slide dengan koma desimal bila presentasi berbahasa Indonesia.
"""
import argparse, math

Z = 1.959964

def wilson(x, n):
    if n == 0:
        return (float("nan"),) * 2
    p = x / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return c - h, c + h

def fmt(x, k=3):
    return "tak terdefinisi" if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))) else f"{x:.{k}f}"

def binary(a):
    ee, ne, ce, nc = a.ee, a.ne, a.ce, a.nc
    eer, cer = ee / ne, ce / nc
    print(f"EER = {ee}/{ne} = {eer*100:.1f}%   CER = {ce}/{nc} = {cer*100:.1f}%")
    # RR dengan CI log
    if ee > 0 and ce > 0:
        rr = eer / cer
        se = math.sqrt(1/ee - 1/ne + 1/ce - 1/nc)
        lo, hi = math.exp(math.log(rr) - Z*se), math.exp(math.log(rr) + Z*se)
        print(f"RR  = {rr:.2f} (95% CI {lo:.2f} sampai {hi:.2f});  RRR = {(1-rr)*100:.1f}%")
    else:
        print("RR  = tidak dihitung (ada sel 0; pakai koreksi 0,5 bila perlu)")
    a_, b_, c_, d_ = ee, ne-ee, ce, nc-ce
    if min(a_, b_, c_, d_) > 0:
        orr = (a_*d_) / (b_*c_)
        se = math.sqrt(1/a_ + 1/b_ + 1/c_ + 1/d_)
        print(f"OR  = {orr:.2f} (95% CI {math.exp(math.log(orr)-Z*se):.2f} sampai {math.exp(math.log(orr)+Z*se):.2f})")
    diff = cer - eer
    se = math.sqrt(eer*(1-eer)/ne + cer*(1-cer)/nc)
    lo, hi = diff - Z*se, diff + Z*se
    harm = a.harm or diff < 0
    if not harm:
        print(f"ARR = {diff*100:.1f}% (95% CI {lo*100:.1f}% sampai {hi*100:.1f}%)")
        nnt = 1/diff
        if lo > 0:
            print(f"NNT = {math.ceil(nnt)} (dari {nnt:.1f}; 95% CI {math.ceil(1/hi)} sampai {math.ceil(1/lo)})")
        else:
            print(f"NNT = {math.ceil(nnt)} (dari {nnt:.1f}); CI ARR melewati 0, jadi CI NNT mencakup NNH. Tulis: tidak bermakna")
    else:
        ari = -diff
        print(f"ARI = {ari*100:.1f}% (95% CI {-hi*100:.1f}% sampai {-lo*100:.1f}%)")
        if ari > 0:
            print(f"NNH = {math.ceil(1/ari)} (dari {1/ari:.1f})")
    print("Kalimat: risiko turun dari {:.1f}% menjadi {:.1f}%; perlu mengobati sekitar {} pasien untuk mencegah 1 kejadian.".format(
        cer*100, eer*100, math.ceil(1/diff) if diff > 0 else "-"))

def diag(a):
    tp, fp, fn, tn = a.tp, a.fp, a.fn, a.tn
    def line(name, x, n):
        lo, hi = wilson(x, n)
        print(f"{name:<14}= {x}/{n} = {x/n*100:.1f}% (95% CI {lo*100:.1f} sampai {hi*100:.1f})")
    line("Sensitivitas", tp, tp+fn)
    line("Spesifisitas", tn, tn+fp)
    line("PPV", tp, tp+fp)
    line("NPV", tn, tn+fn)
    sens, spec = tp/(tp+fn), tn/(tn+fp)
    lrp = sens/(1-spec) if spec < 1 else float("inf")
    lrn = (1-sens)/spec if spec > 0 else float("inf")
    print(f"LR+ = {fmt(lrp,2)}   LR- = {fmt(lrn,2)}   Prevalensi sampel = {(tp+fn)/(tp+fp+fn+tn)*100:.1f}%")
    print("Catatan: PPV/NPV bergantung prevalensi; untuk pasien lokal hitung ulang dengan prevalensi setempat.")

def mean(a):
    md = a.m1 - a.m2
    se = math.sqrt(a.sd1**2/a.n1 + a.sd2**2/a.n2)
    print(f"MD  = {md:.2f} (95% CI {md-Z*se:.2f} sampai {md+Z*se:.2f})  [kelompok 1 dikurangi kelompok 2]")
    sp = math.sqrt(((a.n1-1)*a.sd1**2 + (a.n2-1)*a.sd2**2) / (a.n1+a.n2-2))
    j = 1 - 3/(4*(a.n1+a.n2)-9)
    g = md/sp*j
    seg = math.sqrt((a.n1+a.n2)/(a.n1*a.n2) + g*g/(2*(a.n1+a.n2)))
    print(f"SMD (Hedges g) = {g:.2f} (95% CI {g-Z*seg:.2f} sampai {g+Z*seg:.2f}); 0,2 kecil, 0,5 sedang, 0,8 besar")
    print("Bandingkan MD dengan MCID outcome ini, bukan hanya nilai p.")

def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    b = sp.add_parser("binary"); [b.add_argument(f"--{k}", type=int, required=True) for k in ("ee","ne","ce","nc")]
    b.add_argument("--harm", action="store_true")
    d = sp.add_parser("diag"); [d.add_argument(f"--{k}", type=int, required=True) for k in ("tp","fp","fn","tn")]
    m = sp.add_parser("mean")
    for k in ("m1","sd1","m2","sd2"): m.add_argument(f"--{k}", type=float, required=True)
    for k in ("n1","n2"): m.add_argument(f"--{k}", type=int, required=True)
    a = ap.parse_args()
    {"binary": binary, "diag": diag, "mean": mean}[a.cmd](a)

if __name__ == "__main__":
    main()
