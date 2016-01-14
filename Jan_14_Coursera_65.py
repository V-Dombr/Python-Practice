text = "X-DSPAM-Confidence:    0.8475";

dot_pos = text.find('.')
number = float(text[dot_pos - 1 : ])

print number