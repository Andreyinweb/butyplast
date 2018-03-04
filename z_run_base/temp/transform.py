 # python3 transform.py

file_open = open('nickname.txt', 'r')
file_write = open('worddict.py', 'a')
file_write.write('nickname = [')
i = 1
for word in file_open:
    file_write.write(' "'+ word.rstrip('\n') + '",')
    if (i % 8) == 0:
        file_write.write('\n        ')
    i +=1

file_write.write(' "' + 'End User' + '"]' + '\n' )

file_open.close()
file_write.close()

from worddict import nickname
# print(nickname)
posts = {'title': "Реальность.  Материал из Википедии — свободной энциклопедии",
        'body' : '''Реа́льность (от лат. realis — вещественный, действительный) — философский термин,
употребляющийся в разных значениях как существующее вообще; объективно явленный мир; фрагмент универсума,
составляющий предметную область соответствующей науки; объективно существующие явления, факты,
то есть существующие действительно.
Различают объективную (материальную) реальность и субъективную (явления сознания) реальность.
В диалектическом материализме термин «Реальность» употребляется в двух смыслах:
всё существующее, то есть весь материальный мир, включая все его идеальные продукты;
объективная реальность, то есть материя в совокупности различных её видов.
Реальность противополагается здесь субъективной реальности, то есть явлениям сознания, 
и отождествляется с понятием материи. 
Понятия бытия и реальности изучается разделом философии — онтологией.'''}

print(posts['body'])