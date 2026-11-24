import streamlit as st

st.set_page_config(page_title='KPSS | Demo', page_icon='📚', layout='centered')
st.markdown('''<style>
.stApp {background:#f4f7fc;color:#18243b} [data-testid="stHeader"] {background:#f4f7fc} .stMarkdown h1,.stMarkdown h2,.stMarkdown h3,.stMarkdown p,[data-testid="stWidgetLabel"] p,[data-testid="stMetricValue"], [data-testid="stMetricLabel"] {color:#18243b!important} .stButton button {border-radius:14px;min-height:48px;background:#e3ebff;color:#243047;border:0;font-weight:600} .stButton button:hover {background:#cbdcff;color:#18243b} [data-testid="stRadio"] label p,[data-testid="stCheckbox"] label p {color:#18243b!important} [data-testid="stCaptionContainer"] p {color:#52627a!important} .st-key-menu0 button,.st-key-menu1 button,.st-key-menu2 button,.st-key-menu3 button,.st-key-menu4 button,.st-key-menu5 button,.st-key-menu6 button,.st-key-menu7 button {min-height:100px;font-size:1.05rem;border-radius:18px} .st-key-menu0 button {background:#dce7ff} .st-key-menu1 button {background:#e9dfff} .st-key-menu2 button {background:#ffebc5} .st-key-menu3 button {background:#ffdde5} .st-key-menu4 button {background:#d3f4e7} .st-key-menu5 button {background:#dceeff} .st-key-menu6 button {background:#f0ddff} .st-key-menu7 button {background:#d5f4f4}
</style>''',unsafe_allow_html=True)
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
    st.title('KPSS')
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
    modules=[('📚','Konu Listeleri'),('✍️','Soru Bankası'),('📝','Kendi Notlarım'),('📕','Yanlış Soru Defterim'),('🗺️','Coğrafya Atlası'),('⏱️','Deneme Sınavları'),('💡','Bilgi Kartları'),('📊','Çalışma Takibim')]
    for i in range(0,len(modules),2):
        for j,(col,(icon,name)) in enumerate(zip(st.columns(2),modules[i:i+2])):
            with col:
                if st.button(f'{icon} {name}',use_container_width=True,key=f'menu{i+j}'): go(name)
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
st.caption('V0.2 · Oturumluk demo')
