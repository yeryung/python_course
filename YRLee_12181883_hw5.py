from HW5_pi import pi_num
# pi_num is the string of pi-number defined in HW5_pi.py
digits = '0123456789'
del_chars=['.',' ','\n']
pi_char = '\u03C0'
empty_char=''
for ch in del_chars:
 pi_num = pi_num.replace(ch, empty_char)
n_below_dot = 100
chars_dict = {}
for ch in pi_num[:1+n_below_dot]:
 chars_dict[ch] = chars_dict.get(ch, 0) + 1

print('(1) the length of '+pi_char+' in [HW5_pi.py] =', len(pi_num) )
print('(2) the probability of digits upto [%d]th positions below dot' % n_below_dot)
dgt_lst = [ '+--%s--' % dgt for dgt in digits ]
print( ''.join( dgt_lst )+'+' )
probs = [ '| %4.2f' % (chars_dict[dgt]/(1+n_below_dot)) for dgt in digits ]
print( ''.join( probs )+'|' )
print('+-----'*len(digits)+'+')