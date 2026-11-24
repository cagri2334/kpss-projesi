import streamlit as st

st.set_page_config(page_title='KPSS | Demo', page_icon='📚', layout='wide')
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
.stApp {background:#f2f5fa;color:#17243d;color-scheme:light}
[data-testid="stHeader"] {background:transparent}
#MainMenu, footer, [data-testid="stToolbar"] {visibility:hidden}
.block-container {max-width:960px;padding:3rem 2rem 2rem}
.stApp p,.stApp label,.stApp input,.stApp textarea,.stApp button {font-family:Inter,Arial,sans-serif;color:#17243d}
.stApp h1,.stApp h2,.stApp h3 {font-family:Manrope,Arial,sans-serif;color:#17243d;letter-spacing:-.045em;font-weight:800}
.stApp h1 {font-size:2rem}
[data-testid="stWidgetLabel"] p {font-size:.83rem;font-weight:600;color:#475569}
[data-testid="stCaptionContainer"] p {color:#64748b;font-size:.78rem}
[data-baseweb="select"] > div,[data-baseweb="input"],[data-baseweb="textarea"] {background:white!important;color:#17243d!important;border:1px solid #dce3ef!important;border-radius:12px!important}
[data-baseweb="select"] span,[data-baseweb="select"] input {color:#17243d!important}
.stButton button,.stFormSubmitButton button {background:#5264df;color:white;border:1px solid transparent;border-radius:12px;min-height:46px;font-weight:600;transition:all .18s ease}
.stButton button p,.stFormSubmitButton button p {color:inherit!important;font-weight:600}
.stButton button:hover,.stFormSubmitButton button:hover {background:#4052c9;color:white;border-color:transparent}
.stButton button:disabled {opacity:.5}
[data-testid="stExpander"],[data-testid="stMetric"],[data-testid="stVerticalBlockBorderWrapper"], [data-testid="stForm"] {background:white;border:1px solid #e0e6f0;border-radius:16px}
[data-testid="stMetric"] {padding:18px}
[data-testid="stMetricValue"] {color:#5264df;font-family:Manrope,Arial,sans-serif;font-weight:800}
[data-testid="stMetricLabel"] p {color:#475569}
.brand {display:flex;align-items:center;gap:12px;margin:0 0 18px}
.brand-mark {display:grid;place-items:center;width:46px;height:46px;border-radius:14px;background:#5264df;color:white;font:800 25px Manrope,Arial,sans-serif}
.brand-name {font:800 32px Manrope,Arial,sans-serif;letter-spacing:-2px;color:#17243d}
[class*="st-key-menu"] button {background:#fff;color:#17243d;border:1px solid #dfe5ef;border-radius:18px;min-height:108px;justify-content:flex-start;text-align:left;padding:18px;box-shadow:0 4px 14px #17243d08}
[class*="st-key-menu"] button p {font-family:Manrope,Arial,sans-serif;font-size:1rem;font-weight:800;line-height:1.35;text-align:left}
[class*="st-key-menu"] button:hover {background:#eef1ff;color:#4052c9;border-color:#aab5f2;transform:translateY(-2px)}
.st-key-menu8 button {background:#17243d;color:white;min-height:88px;border-color:#17243d}
.st-key-menu8 button:hover {background:#26395c;color:white}
@media(max-width:600px) {.block-container {padding:2rem 1rem 1.5rem}.stApp h1 {font-size:1.65rem} [data-testid="stHorizontalBlock"]:has([class*="st-key-menu"]) {flex-wrap:nowrap!important;gap:10px!important} [data-testid="stHorizontalBlock"]:has([class*="st-key-menu"]) > [data-testid="stColumn"] {width:calc(50% - 5px)!important;min-width:0!important;flex:1 1 0!important} [class*="st-key-menu"] button {min-height:100px;padding:12px} [class*="st-key-menu"] button p {font-size:.88rem}}
</style>""",unsafe_allow_html=True)
TOPICS={
'Türkçe':['Sözcükte anlam','Cümlede anlam','Paragraf','Ses bilgisi','Sözcük türleri','Cümlenin ögeleri','Yazım kuralları','Noktalama','Sözel mantık'],
'Matematik':['Temel kavramlar','Sayılar','Bölünebilme','Rasyonel sayılar','Üslü ve köklü sayılar','Denklemler','Oran ve orantı','Problemler','Sayısal mantık','Geometri'],
'Tarih':['İslamiyet öncesi Türk tarihi','Türk-İslam devletleri','Osmanlı tarihi','Osmanlı kültür ve medeniyeti','Kurtuluş Savaşı','Atatürk ilke ve inkılapları','Çağdaş Türk ve dünya tarihi'],
'Coğrafya':['Coğrafi konum','Yer şekilleri','Dağlar, ovalar ve platolar','Akarsular ve göller','İklim ve bitki örtüsü','Nüfus ve yerleşme','Tarım ve hayvancılık','Madenler ve enerji','Sanayi','Ulaşım ve ticaret','Turizm','Bölgeler coğrafyası'],
'Vatandaşlık':['Hukukun temel kavramları','Anayasa hukuku','Temel hak ve özgürlükler','Yasama','Yürütme','Yargı','İdare hukuku'],
'Güncel Bilgiler':['Türkiye ve dünya gündemi','Kültür ve sanat','Bilim ve teknoloji']}
QUESTIONS=[('Coğrafya','Tamamı Türkiye sınırları içinde kalan en uzun akarsu hangisidir?',['Fırat','Dicle','Kızılırmak','Sakarya','Yeşilırmak'],2,'Kızılırmak tamamen Türkiye sınırları içinde akar.'),('Tarih','Türkiye Büyük Millet Meclisi hangi tarihte açılmıştır?',['19 Mayıs 1919','23 Nisan 1920','29 Ekim 1923','30 Ağustos 1922','24 Temmuz 1923'],1,'TBMM 23 Nisan 1920 tarihinde Ankara’da açılmıştır.'),('Matematik','Bir sayının yüzde 25’i 15 ise sayı kaçtır?',['30','45','50','60','75'],3,'15 / 0,25 = 60.'),('Türkçe','Hangisi eş anlamlı bir sözcük çiftidir?',['Gece – gündüz','Az – çok','Uzak – yakın','Kara – siyah','İleri – geri'],3,'Kara ve siyah renk anlamında eş anlamlıdır.'),('Vatandaşlık','Türkiye’de yasama yetkisi hangi organa aittir?',['Danıştay','Yargıtay','TBMM','Sayıştay','Anayasa Mahkemesi'],2,'Anayasa’nın 7. maddesine göre yasama yetkisi TBMM’ye aittir.')]
for k,v in {'page':'Ana Sayfa','done':{},'answers':{},'q':0,'exam':0,'notes':{},'wrong':{},'retry':0,'practice':0}.items():
    if k not in st.session_state: st.session_state[k]=v
s=st.session_state
if s.page == 'Ana Sayfa':
    st.markdown('<div class="brand"><div class="brand-mark">K</div><div class="brand-name">KPSS</div></div>',unsafe_allow_html=True)
level=st.selectbox('Sınav seviyen',['Ortaöğretim','Ön Lisans','Lisans'],key='level')
def go(page):
    s.page=page
    if page in ['Soru Bankası','Deneme Sınavları']: s.q=0
    if page=='Deneme Sınavları': s.exam+=1
    if page=='Soru Bankası': s.practice+=1
    st.rerun()
if s.page!='Ana Sayfa':
    if st.button('← Ana sayfa'): go('Ana Sayfa')
if s.page=='Ana Sayfa':
    modules=[('menu_book','Konu Listeleri'),('quiz','Soru Bankası'),('edit_note','Kendi Notlarım'),('assignment_late','Yanlış Soru Defterim'),('public','Coğrafya Atlası'),('timer','Deneme Sınavları'),('style','Bilgi Kartları'),('monitoring','Çalışma Takibim')]
    for i in range(0,len(modules),2):
        for j,(col,(icon,name)) in enumerate(zip(st.columns(2),modules[i:i+2])):
            with col:
                if st.button(name,icon=f':material/{icon}:',use_container_width=True,key=f'menu{i+j}'): go(name)
    if st.button('Kariyer ve Atama Merkezi',icon=':material/work_outline:',use_container_width=True,key='menu8'): go('Kariyer ve Atama Merkezi')
elif s.page=='Kariyer ve Atama Merkezi':
    st.title('Kariyer ve Atama Merkezi')
    st.caption('Ar-Ge demosu · Aşağıdaki ilanlar ve puanlar tamamen kurgusaldır.')
    if 'career_saved' not in s: s.career_saved=[]
    if 'career_profile' not in s: s.career_profile={}
    profile=s.career_profile.get(level,{})
    listings=[
        dict(id=1,title='Örnek büro personeli',level='Lisans',city='Ankara',score=70,department='İşletme',kind='Sözleşmeli personel',past=82),
        dict(id=2,title='Örnek memur',level='Ön Lisans',city='Elazığ',score=65,department='Tüm bölümler',kind='Memur',past=76),
        dict(id=3,title='Örnek destek personeli',level='Ortaöğretim',city='Malatya',score=60,department='Tüm bölümler',kind='Sözleşmeli personel',past=72),
        dict(id=4,title='Örnek idari personel',level='Lisans',city='İstanbul',score=75,department='Tüm bölümler',kind='Memur',past=85)]
    section=st.radio('Bölüm',['Alım Haberleri','Kişisel Alım Radarı','Tercih Danışmanlığı','Geçmiş Puanlar','Başvuru Takvimim','Kaydedilen İlanlar'],key='career_section')
    def matches(item):
        return bool(profile) and item['level']==level and item['score']<=profile['score'] and (profile['city']=='Tüm Türkiye' or item['city']==profile['city']) and (item['department']=='Tüm bölümler' or item['department'].casefold()==profile['department'].strip().casefold()) and item['kind'] in profile['kinds']
    def show_listing(item):
        with st.container(border=True):
            st.subheader(item['title'])
            st.write(f"{item['city']} · {item['level']} · {item['kind']}")
            st.write(f"Örnek taban başvuru puanı: {item['score']} · Bölüm: {item['department']}")
            if matches(item): st.success('Demo filtrelerinle eşleşiyor.')
            saved=item['id'] in s.career_saved
            if st.button('Kaydı kaldır' if saved else 'İlanı kaydet',key=f"career_{section}_{item['id']}"):
                if saved: s.career_saved.remove(item['id'])
                else: s.career_saved.append(item['id'])
                st.rerun()
    if section=='Alım Haberleri':
        for item in listings: show_listing(item)
        st.markdown('Resmî kaynaklar: [ÖSYM](https://www.osym.gov.tr/) · [Kariyer Kapısı](https://kariyerkapisi.gov.tr/) · [Resmî Gazete](https://www.resmigazete.gov.tr/)')
    elif section=='Kişisel Alım Radarı':
        with st.form('radar_'+level):
            department=st.text_input('Mezuniyet bölümü',value=profile.get('department',''))
            score=st.number_input('KPSS puanı',min_value=0.0,max_value=100.0,value=float(profile.get('score',75)))
            cities=['Tüm Türkiye','Ankara','Elazığ','Malatya','İstanbul']
            city=st.selectbox('Şehir',cities,index=cities.index(profile.get('city','Tüm Türkiye')))
            kinds=st.multiselect('Kadro türleri',['Memur','Sözleşmeli personel'],default=profile.get('kinds',['Memur','Sözleşmeli personel']))
            notify=st.checkbox('Bildirim almak istiyorum (demo tercihi)',value=profile.get('notify',False))
            if st.form_submit_button('Filtreleri kaydet'):
                s.career_profile[level]=dict(department=department,score=score,city=city,kinds=kinds,notify=notify)
                st.rerun()
        st.caption('Gerçek telefon bildirimi gönderilmez.')
        found=[item for item in listings if matches(item)]
        st.metric('Eşleşen örnek ilan',len(found))
        for item in found: show_listing(item)
    elif section=='Tercih Danışmanlığı':
        st.info('Örnek puan karşılaştırmasıdır; atanma olasılığı veya garantisi değildir.')
        if not profile: st.warning('Önce Kişisel Alım Radarı bölümünde profilini oluştur.')
        else:
            found=[item for item in listings if matches(item)]
            if not found: st.write('Filtrelerine uygun örnek kadro yok.')
            for item in found:
                with st.container(border=True):
                    st.subheader(item['title'])
                    diff=profile['score']-item['past']
                    st.metric('Kurgusal geçmiş puana göre fark',f'{diff:+.1f}')
                    st.write('Geçmiş örnek puanın üzerinde' if diff>=0 else 'Geçmiş örnek puanın altında')
        st.caption('Gerçek danışmanlıkta puan türü, nitelik kodları ve resmî kılavuz doğrulanmalıdır.')
    elif section=='Geçmiş Puanlar':
        for item in listings:
            if item['level']==level: st.metric(item['title']+' · Kurgusal geçmiş puan',item['past'])
    elif section=='Başvuru Takvimim':
        if 'career_dates' not in s: s.career_dates=[]
        with st.form('career_date'):
            title=st.text_input('Başvuru / hatırlatma adı')
            date=st.date_input('Son başvuru tarihi')
            if st.form_submit_button('Takvime ekle') and title.strip():
                s.career_dates.append((title.strip(),date)); st.rerun()
        for i,(title,date) in enumerate(s.career_dates):
            st.write(f'{date:%d.%m.%Y} · {title}')
            if st.button('Sil',key=f'career_date_delete_{i}'):
                s.career_dates.pop(i); st.rerun()
        st.caption('Takvim oturumluk kayıt tutar; otomatik hatırlatma göndermez.')
    else:
        if not s.career_saved: st.info('Henüz kayıtlı ilan yok.')
        for item in listings:
            if item['id'] in s.career_saved: show_listing(item)
elif s.page=='Konu Listeleri':
    st.title('Konu Listeleri')
    subject=st.selectbox('Ders seç',list(TOPICS))
    topics=TOPICS[subject]
    for topic in topics:
        key=f'{level}|{subject}|{topic}'
        checked=st.checkbox(topic,value=s.done.get(key,False),key='topic_'+key)
        s.done[key]=checked
    count=sum(s.done.get(f'{level}|{subject}|{t}',False) for t in topics)
    st.progress(count/len(topics),text=f'{count}/{len(topics)} konu tamamlandı')
    st.caption('Örnek konu listesi; resmî müfredat doğrulaması henüz yapılmadı.')
elif s.page in ['Soru Bankası','Deneme Sınavları']:
    st.title(s.page)
    exam=s.page=='Deneme Sınavları'
    st.caption('5 soruluk mini deneme (süresiz)' if exam else 'Özgün örnek sorular')
    if s.q>=len(QUESTIONS):
        st.success('Sorular tamamlandı!')
        if st.button('Başa dön'): go(s.page)
    else:
        subject,question,options,correct,explanation=QUESTIONS[s.q]
        key=f'{level}|{s.page}|{s.exam if exam else s.practice}|{s.q}'
        st.progress((s.q+1)/len(QUESTIONS),text=f'Soru {s.q+1}/{len(QUESTIONS)} · {subject}')
        st.subheader(question)
        choice=st.radio('Cevabın',range(5),format_func=lambda i:f'{chr(65+i)}) {options[i]}',index=None,key='radio_'+key,disabled=key in s.answers)
        if st.button('Cevabı kontrol et',disabled=choice is None or key in s.answers):
            s.answers[key]=(choice==correct,choice)
            if choice!=correct: s.wrong[(level,s.q)]=choice
            st.rerun()
        if key in s.answers:
            if s.answers[key][0]: st.success('Doğru cevap!')
            else: st.error('Yanlış cevap. Doğru seçenek: '+options[correct])
            st.info(explanation)
            if st.button('Sonraki soru'): s.q+=1; st.rerun()
elif s.page=='Kendi Notlarım':
    st.title('Kendi Notlarım')
    subject=st.selectbox('Ders',list(TOPICS),key='note_subject')
    topic=st.radio('Konular',TOPICS[subject],key='note_topic_'+subject)
    nk=(level,subject,topic)
    st.subheader(topic)
    for i,note in enumerate(s.notes.get(nk,[])):
        with st.container(border=True):
            edited=st.text_area('Not',note,key=f'edit_{nk}_{i}')
            a,b=st.columns(2)
            if a.button('Güncelle',key=f'update_{nk}_{i}'):
                s.notes[nk][i]=edited; st.rerun()
            if b.button('Sil',key=f'delete_{nk}_{i}'):
                s.notes[nk].pop(i)
                for k in list(s.keys()):
                    if k.startswith(f'edit_{nk}_'): del s[k]
                st.rerun()
    with st.form('new_note',clear_on_submit=True):
        note=st.text_area('Yeni not')
        if st.form_submit_button('Not ekle') and note.strip():
            s.notes.setdefault(nk,[]).append(note.strip()); st.rerun()
    st.caption('Notlar bu oturumda saklanır.')
elif s.page=='Yanlış Soru Defterim':
    st.title('Yanlış Soru Defterim')
    ids=[i for (lev,i) in s.wrong if lev==level]
    st.metric('Tekrar edilecek soru',len(ids))
    subject=st.selectbox('Ders',['Tümü']+list(TOPICS),key='wrong_subject')
    if not ids: st.info('Henüz yanlış soru yok.')
    for i in ids:
        sub,question,options,correct,explanation=QUESTIONS[i]
        if subject!='Tümü' and subject!=sub: continue
        with st.expander(sub+' · '+question):
            st.caption('Önceki cevabın: '+options[s.wrong[(level,i)]])
            choice=st.radio('Tekrar çöz',range(5),format_func=lambda j: f'{chr(65+j)}) {options[j]}',index=None,key=f'retry_{level}_{i}_{s.retry}')
            if st.button('Kontrol et',key=f'check_{level}_{i}',disabled=choice is None):
                if choice==correct: st.success('Doğru! '+explanation)
                else: st.error('Doğru cevap: '+options[correct]+'. '+explanation)
            if st.button('Öğrendim, defterden çıkar',key=f'remove_{level}_{i}'):
                del s.wrong[(level,i)]; s.retry+=1; st.rerun()
elif s.page=='Coğrafya Atlası':
    st.title('Coğrafya Atlası')
    places={'Akarsular':{'Kızılırmak':(40.0,34.0,'Tamamı Türkiye sınırları içinde kalan en uzun akarsu.'),'Fırat':(38.7,39.0,'Doğu Anadolu’dan doğar, Basra Körfezi havzasına ulaşır.')},'Göller':{'Van Gölü':(38.6,42.9,'Türkiye’nin yüzölçümü en büyük gölü.'),'Tuz Gölü':(38.75,33.4,'İç Anadolu’da bulunan tuzlu göl.')},'Dağlar':{'Ağrı Dağı':(39.7,44.3,'Türkiye’nin en yüksek dağı.'),'Erciyes':(38.53,35.45,'Kayseri’de bulunan volkanik dağ.')}}
    category=st.selectbox('Harita katmanı',list(places))
    items=places[category]
    st.map([{'lat':v[0],'lon':v[1]} for v in items.values()],zoom=4)
    name=st.selectbox('Coğrafi unsur',list(items))
    st.info(items[name][2])
    st.caption('Yaklaşık konum işaretleri. Fiziki harita ve akarsu çizgileri henüz yok.')
elif s.page=='Bilgi Kartları':
    st.title('Bilgi Kartları')
    for subject,question,options,correct,explanation in QUESTIONS:
        with st.expander(subject+' · '+question): st.write(options[correct]); st.write(explanation)
else:
    st.title('Çalışma Takibim')
    answers=[v for k,v in s.answers.items() if k.startswith(level+'|')]
    correct=sum(v[0] for v in answers)
    a,b=st.columns(2); a.metric('Doğru',correct); b.metric('Yanlış',len(answers)-correct)
    st.metric('Tamamlanan konu',sum(v for k,v in s.done.items() if k.startswith(level+'|')))
    if answers: st.progress(correct/len(answers),text=f'Başarı: %{round(100*correct/len(answers))}')
    st.caption('Veriler yalnızca mevcut oturumda tutulur.')
st.divider()
st.caption('V0.5 · Oturumluk demo')
