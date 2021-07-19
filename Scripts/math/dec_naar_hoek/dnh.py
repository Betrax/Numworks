dec_hoek = float(input())
uur_hoek = dec_hoek // 1
dec_hoek -= uur_hoek

min_hoek = dec_hoek * 60 // 1
dec_hoek -= min_hoek / 60

sec_hoek = dec_hoek * 3600
print("{}, {}', {}''".format(int(uur_hoek), int(min_hoek), sec_hoek))
