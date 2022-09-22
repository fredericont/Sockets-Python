import feedparser

COR_TEXTO_1 = '\033[91m' # Vermelho
COR_TEXTO_2 = '\033[92m' # Verde
COR_TEXTO_3 = '\033[93m' # Amarelo
COR_TEXTO_4 = '\033[94m' # Azul 
COR_PADRAO  = '\033[0m'  # Reseta a cor

br = []
br_url = 'http://g1.globo.com/dynamo/brasil/rss2.xml'
brG1 = feedparser.parse(br_url)

for c in brG1.entries[0:10]:    
    br.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Noticias do Brasil' + COR_PADRAO))
    br.append(c.links[0].href)
    br.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
brTrat = ('\n'.join(map(str, br)))


car = []
car_url = 'http://g1.globo.com/dynamo/carros/rss2.xml'
carG1 = feedparser.parse(car_url)

for c in carG1.entries[0:10]:    
    car.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Carros' + COR_PADRAO))
    car.append(c.links[0].href)
    car.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
carTrat = ('\n'.join(map(str, car)))

cs = []
cs_url = 'http://g1.globo.com/dynamo/ciencia-e-saude/rss2.xml'
csG1 = feedparser.parse(cs_url)

for c in carG1.entries[0:10]:    
    cs.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Ciência e Saúde' + COR_PADRAO))
    cs.append(c.links[0].href)
    cs.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
csTrat = ('\n'.join(map(str, cs)))


ce = []
ce_url = ' http://g1.globo.com/dynamo/concursos-e-emprego/rss2.xml'
ceG1 = feedparser.parse(ce_url)

for c in carG1.entries[0:10]:    
    ce.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Concuros e Empregos' + COR_PADRAO))
    ce.append(c.links[0].href)
    ce.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
ceTrat = ('\n'.join(map(str, ce)))


e = []
e_url = 'http://g1.globo.com/dynamo/economia/rss2.xml'
eG1 = feedparser.parse(e_url)

for c in eG1.entries[0:10]:    
    e.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Economia' + COR_PADRAO))
    e.append(c.links[0].href)
    e.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
eTrat = ('\n'.join(map(str, e)))


edu = []
edu_url = 'http://g1.globo.com/dynamo/educacao/rss2.xml'
eduG1 = feedparser.parse(edu_url)

for c in eduG1.entries[0:10]:    
    edu.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Educação' + COR_PADRAO))
    edu.append(c.links[0].href)
    edu.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
eduTrat = ('\n'.join(map(str, edu)))


loto = []
loto_url = 'http://g1.globo.com/dynamo/loterias/rss2.xml'
lotoG1 = feedparser.parse(loto_url)

for c in lotoG1.entries[0:10]:    
    loto.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Loteria' + COR_PADRAO))
    loto.append(c.links[0].href)
    loto.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
lotoTrat = ('\n'.join(map(str, loto)))


mundo = []
mundo_url = 'http://g1.globo.com/dynamo/mundo/rss2.xml'
mundoG1 = feedparser.parse(mundo_url)

for c in mundoG1.entries[0:10]:    
    mundo.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Notícias do Mundo' + COR_PADRAO))
    mundo.append(c.links[0].href)
    mundo.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
mundoTrat = ('\n'.join(map(str, mundo)))


m = []
m_url = 'http://g1.globo.com/dynamo/musica/rss2.xml'
mG1 = feedparser.parse(m_url)

for c in mG1.entries[0:10]:    
    m.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Musicas' + COR_PADRAO))
    m.append(c.links[0].href)
    m.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
mTrat = ('\n'.join(map(str, m)))


nat = []
nat_url = 'http://g1.globo.com/dynamo/natureza/rss2.xml'
natG1 = feedparser.parse(nat_url)

for c in natG1.entries[0:10]:    
    nat.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Natureza' + COR_PADRAO))
    nat.append(c.links[0].href)
    nat.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
natTrat = ('\n'.join(map(str, nat)))


p = []
p_url = 'http://g1.globo.com/dynamo/politica/mensalao/rss2.xml'
pG1 = feedparser.parse(p_url)

for c in pG1.entries[0:10]:    
    p.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Política' + COR_PADRAO))
    p.append(c.links[0].href)
    p.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
pTrat = ('\n'.join(map(str, p)))


pop = []
pop_url = 'http://g1.globo.com/dynamo/pop-arte/rss2.xml'
popG1 = feedparser.parse(pop_url)

for c in popG1.entries[0:10]:    
    pop.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Pop e Arte' + COR_PADRAO))
    pop.append(c.links[0].href)
    pop.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
popTrat = ('\n'.join(map(str, pop)))


tech = []
tech_url = 'http://g1.globo.com/dynamo/tecnologia/rss2.xml'
techG1 = feedparser.parse(tech_url)

for c in techG1.entries[0:10]:    
    tech.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Tecnologia e Games' + COR_PADRAO))
    tech.append(c.links[0].href)
    tech.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
techTrat = ('\n'.join(map(str, tech)))

tur = []
tur_url = 'http://g1.globo.com/dynamo/turismo-e-viagem/rss2.xml'
turG1 = feedparser.parse(tur_url)

for c in turG1.entries[0:10]:    
    tur.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Turismo' + COR_PADRAO))
    tur.append(c.links[0].href)
    tur.append(('---------------------------------------------------------------------------------'))

# Tratando os dados da lista, e convertendo em string
turTrat = ('\n'.join(map(str, tur)))


'''
 Fim das notícias divididas por categorias

 Abaixo, consulta e tratamento de notícias subdivídidos por estados brasileiros. 
'''

ac = []
ac_url = 'http://g1.globo.com/dynamo/ac/acre/rss2.xml'
acG1 = feedparser.parse(ac_url)
for c in acG1.entries[0:10]:    
    ac.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Acre' + COR_PADRAO))
    ac.append(c.links[0].href)
    ac.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
acTrat = ('\n'.join(map(str, ac)))

al = []
al_url = 'http://g1.globo.com/dynamo/al/alagoas/rss2.xml'
alG1 = feedparser.parse(al_url)
for c in alG1.entries[0:10]:    
    al.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Alagoas' + COR_PADRAO))
    al.append(c.links[0].href)
    al.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
alTrat = ('\n'.join(map(str, al)))

ap = []
ap_url = 'http://g1.globo.com/dynamo/ap/amapa/rss2.xml'
apG1 = feedparser.parse(ap_url)
for c in apG1.entries[0:10]:    
    ap.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Amapá' + COR_PADRAO))
    ap.append(c.links[0].href)
    ap.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
apTrat = ('\n'.join(map(str, ap)))

am = []
am_url = 'http://g1.globo.com/dynamo/am/amazonas/rss2.xml'
amG1 = feedparser.parse(am_url)
for c in amG1.entries[0:10]:    
    am.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Amazonas' + COR_PADRAO))
    am.append(c.links[0].href)
    am.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
amTrat = ('\n'.join(map(str, am)))

ba = []
ba_url = 'http://g1.globo.com/dynamo/bahia/rss2.xml'
baG1 = feedparser.parse(ba_url)
for c in baG1.entries[0:10]:    
    ba.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Bahia' + COR_PADRAO))
    ba.append(c.links[0].href)
    ba.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
baTrat = ('\n'.join(map(str, ba)))

ce = []
ce_url = 'http://g1.globo.com/dynamo/ceara/rss2.xml'
ceG1 = feedparser.parse(ce_url)
for c in ceG1.entries[0:10]:    
    ce.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Ceará' + COR_PADRAO))
    ce.append(c.links[0].href)
    ce.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
ceTrat = ('\n'.join(map(str, ce)))

df = []
df_url = 'http://g1.globo.com/dynamo/distrito-federal/rss2.xml'
dfG1 = feedparser.parse(df_url)
for c in dfG1.entries[0:10]:    
    df.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Distrito Federal' + COR_PADRAO))
    df.append(c.links[0].href)
    df.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
dfTrat = ('\n'.join(map(str, df)))

es = []
es_url = 'http://g1.globo.com/dynamo/espirito-santo/rss2.xml'
esG1 = feedparser.parse(es_url)
for c in esG1.entries[0:10]:    
    es.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Espírito Santo' + COR_PADRAO))
    es.append(c.links[0].href)
    es.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
esTrat = ('\n'.join(map(str, es)))

go = []
go_url = 'http://g1.globo.com/dynamo/goias/rss2.xml'
goG1 = feedparser.parse(go_url)
for c in goG1.entries[0:10]:    
    go.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Goiás' + COR_PADRAO))
    go.append(c.links[0].href)
    go.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
goTrat = ('\n'.join(map(str, go)))


ma = []
ma_url = 'http://g1.globo.com/dynamo/ma/maranhao/rss2.xml'
maG1 = feedparser.parse(ma_url)
for c in maG1.entries[0:10]:    
    ma.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Maranhão' + COR_PADRAO))
    ma.append(c.links[0].href)
    ma.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
maTrat = ('\n'.join(map(str, ma)))

mt = []
mt_url = 'http://g1.globo.com/dynamo/mato-grosso/rss2.xml'
mtG1 = feedparser.parse(mt_url)
for c in mtG1.entries[0:10]:    
    mt.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Mato Grosso' + COR_PADRAO))
    mt.append(c.links[0].href)
    mt.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
mtTrat = ('\n'.join(map(str, mt)))

ms = []
ms_url = 'http://g1.globo.com/dynamo/mato-grosso-do-sul/rss2.xml'
msG1 = feedparser.parse(ms_url)
for c in msG1.entries[0:10]:    
    ms.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Mato Grosso do Sul' + COR_PADRAO))
    ms.append(c.links[0].href)
    ms.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
msTrat = ('\n'.join(map(str, ms)))

mg = []
mg_url = 'http://g1.globo.com/dynamo/minas-gerais/rss2.xml'
mgG1 = feedparser.parse(mg_url)
for c in mgG1.entries[0:10]:    
    mg.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Minas Gerais' + COR_PADRAO))
    mg.append(c.links[0].href)
    mg.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
mgTrat = ('\n'.join(map(str, mg)))

pa = []
pa_url = 'http://g1.globo.com/dynamo/pa/para/rss2.xml'
paG1 = feedparser.parse(pa_url)
for c in paG1.entries[0:10]:    
    pa.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Pará' + COR_PADRAO))
    pa.append(c.links[0].href)
    pa.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
paTrat = ('\n'.join(map(str, pa)))

pb = []
pb_url = 'http://g1.globo.com/dynamo/pb/paraiba/rss2.xml'
pbG1 = feedparser.parse(pb_url)
for c in pbG1.entries[0:10]:    
    pb.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Paraíba' + COR_PADRAO))
    pb.append(c.links[0].href)
    pb.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
pbTrat = ('\n'.join(map(str, pb)))

pr = []
pr_url = 'http://g1.globo.com/dynamo/pr/parana/rss2.xml'
prG1 = feedparser.parse(pr_url)
for c in prG1.entries[0:10]:    
    pr.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Paraná' + COR_PADRAO))
    pr.append(c.links[0].href)
    pr.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
prTrat = ('\n'.join(map(str, pr)))

pe = []
pe_url = 'http://g1.globo.com/dynamo/pernambuco/rss2.xml'
peG1 = feedparser.parse(pe_url)
for c in peG1.entries[0:10]:    
    pe.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Pernambuco' + COR_PADRAO))
    pe.append(c.links[0].href)
    pe.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
peTrat = ('\n'.join(map(str, pe)))

rj = []
rj_url = 'http://g1.globo.com/dynamo/rio-de-janeiro/rss2.xml'
rjG1 = feedparser.parse(rj_url)
for c in rjG1.entries[0:10]:    
    rj.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Rio de Janeiro' + COR_PADRAO))
    rj.append(c.links[0].href)
    rj.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
rjTrat = ('\n'.join(map(str, rj)))

rn = []
rn_url = 'http://g1.globo.com/dynamo/rn/rio-grande-do-norte/rss2.xml'
rnG1 = feedparser.parse(rn_url)
for c in rnG1.entries[0:10]:    
    rn.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Rio Grande do Norte' + COR_PADRAO))
    rn.append(c.links[0].href)
    rn.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
rnTrat = ('\n'.join(map(str, rn)))

rs = []
rs_url = 'http://g1.globo.com/dynamo/rs/rio-grande-do-sul/rss2.xml'
rsG1 = feedparser.parse(rs_url)
for c in rsG1.entries[0:10]:    
    rs.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Rio Grande do Sul' + COR_PADRAO))
    rs.append(c.links[0].href)
    rs.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
rsTrat = ('\n'.join(map(str, rs)))

ro = []
ro_url = 'http://g1.globo.com/dynamo/ro/rondonia/rss2.xml'
roG1 = feedparser.parse(ro_url)
for c in roG1.entries[0:10]:    
    ro.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Rondônia' + COR_PADRAO))
    ro.append(c.links[0].href)
    ro.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
roTrat = ('\n'.join(map(str, ro)))

rr = []
rr_url = 'http://g1.globo.com/dynamo/rr/roraima/rss2.xml'
rrG1 = feedparser.parse(rr_url)
for c in rrG1.entries[0:10]:    
    rr.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Roraima' + COR_PADRAO))
    rr.append(c.links[0].href)
    rr.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
rrTrat = ('\n'.join(map(str, rr)))

sc = []
sc_url = 'http://g1.globo.com/dynamo/sc/santa-catarina/rss2.xml'
scG1 = feedparser.parse(sc_url)
for c in scG1.entries[0:10]:    
    sc.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Santa Catarina' + COR_PADRAO))
    sc.append(c.links[0].href)
    sc.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
scTrat = ('\n'.join(map(str, sc)))

sp = []
sp_url = 'http://g1.globo.com/dynamo/sao-paulo/rss2.xml'
spG1 = feedparser.parse(sp_url)
for c in spG1.entries[0:10]:    
    sp.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | São Paulo' + COR_PADRAO))
    sp.append(c.links[0].href)
    sp.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
spTrat = ('\n'.join(map(str, sp)))

se = []
se_url = 'http://g1.globo.com/dynamo/se/sergipe/rss2.xml'
seG1 = feedparser.parse(se_url)
for c in seG1.entries[0:10]:    
    se.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Sergipe' + COR_PADRAO))
    se.append(c.links[0].href)
    se.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
seTrat = ('\n'.join(map(str, se)))

to = []
to_url = 'http://g1.globo.com/dynamo/to/tocantins/rss2.xml'
toG1 = feedparser.parse(to_url)
for c in toG1.entries[0:10]:    
    to.append(str(COR_TEXTO_4 + c.title + COR_PADRAO + COR_TEXTO_3 + ' | Tocantins' + COR_PADRAO))
    to.append(c.links[0].href)
    to.append(('---------------------------------------------------------------------------------'))
# Tratando os dados da lista, e convertendo em string
toTrat = ('\n'.join(map(str, to)))

