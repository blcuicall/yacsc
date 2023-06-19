# -*- coding:UTF-8 -*-

from argparse import ArgumentParser

def read_lines(path):
    lines = []
    with open(path, "r", encoding="utf8") as fr:
        for line in fr:
            line = line.strip()
            if not line:
                continue
            lines.append(line)
    return lines

def main(args):
    fw = open(args.out, "w", encoding="utf8")
    sent_id = 0
    for src_line ,trg_line in zip(read_lines(args.src), read_lines(args.trg)):
        labels = [str(sent_id)]
        assert len(src_line) == len(trg_line)
        for char_id, (src_char, trg_char) in enumerate(zip(src_line, trg_line)):
            # if src_char == trg_char or trg_char in list("她他它"):
            if src_char == trg_char:
                continue
            else:
                labels.extend([str(char_id+1), trg_char])
        if len(labels) == 1:
            labels.append("0")
        fw.write(", ".join(labels)+"\n")
        sent_id += 1
    fw.close()
        

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--src")
    parser.add_argument("--trg")
    parser.add_argument("--out")
    args = parser.parse_args()
    main(args)
