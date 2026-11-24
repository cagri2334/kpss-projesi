import streamlit as st

st.set_page_config(page_title='KPSS | Demo', page_icon='📚', layout='wide')
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');
.stApp {background:#f2f5fa;color:#17243d;color-scheme:light}
[data-testid="stHeader"] {background:transparent}
#MainMenu, footer, [data-testid="stToolbar"] {visibility:hidden}
.block-container {max-width:960px;padding:3rem 2rem 2rem}
.stApp p,.stApp label,.stApp input,.stApp textarea,.stApp button {font-family:Manrope,Arial,sans-serif;color:#17243d}
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

.hero {background:linear-gradient(125deg,#24346b,#5264df);border-radius:24px;padding:26px;color:white;margin:8px 0 16px;box-shadow:0 12px 30px #26366c22}
.hero small {color:#dce4ff;font:600 12px Manrope,Arial;letter-spacing:1px}.hero strong {display:block;font:800 30px Manrope,Arial;margin:10px 0}.hero span {color:#e5eaff;font:400 14px Manrope,Arial}
[class*="st-key-nav"] button {background:white;color:#5264df;border:1px solid #dfe5ef;min-height:44px;padding:5px;font-size:12px}
@media(max-width:600px){[data-testid="stHorizontalBlock"]:has([class*="st-key-nav"]){flex-wrap:nowrap!important;gap:4px!important}[data-testid="stHorizontalBlock"]:has([class*="st-key-nav"]) > [data-testid="stColumn"]{min-width:0!important;flex:1 1 0!important;width:19%!important}[class*="st-key-nav"] button p{font-size:10px!important}[class*="st-key-nav"] button{padding:4px!important}.hero{padding:20px}.hero strong{font-size:25px}}

.stApp {background:#f6f8fc}
.stApp p,.stApp label,.stApp input,.stApp textarea,.stApp button {font-family:Manrope,Arial,sans-serif}
.block-container {max-width:820px;padding-top:2.4rem}
.stApp h1 {font-size:1.8rem;letter-spacing:-.035em}
.stApp h2,.stApp h3 {font-size:1.15rem;letter-spacing:-.02em}
.brand {margin-bottom:8px}.brand-name {font-size:27px}.brand-mark {width:38px;height:38px;font-size:21px;border-radius:11px}
[class*="st-key-nav"] button {min-height:48px;border-radius:10px;color:#475569;background:#fff;box-shadow:none}
[class*="st-key-nav"] button[data-testid="stBaseButton-primary"] {background:#26366c;color:white;border-color:#26366c}
[class*="st-key-nav"] button p {font-weight:700;font-size:.82rem}
[class*="st-key-menu"] button {min-height:84px;border-radius:14px;box-shadow:none;padding:15px}
[class*="st-key-menu"] button p {font-weight:700;font-size:.95rem}
.hero {background:#26366c;border-radius:18px;box-shadow:none;padding:22px}
.hero small {letter-spacing:0;font-size:13px}.hero strong {font-size:26px}
@media(max-width:600px){.block-container{padding:1.5rem .85rem}.stApp h1{font-size:1.55rem}[class*="st-key-nav"] button p{font-size:10px!important;overflow-wrap:normal;line-height:1.2}[class*="st-key-menu"] button{min-height:84px;padding:10px}[class*="st-key-menu"] button p{font-size:.83rem}.hero{padding:18px}}

.stApp {background:radial-gradient(ellipse at 90% 0%,#e5eaff 0%,#f7f9fc 45%);}
.block-container {max-width:900px;padding-top:2rem}
.orbit-panel {background:radial-gradient(ellipse at 75% 30%,#344c93,#101a38 70%);border-radius:28px;padding:28px;color:#fff;overflow:hidden;display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:230px;box-shadow:0 16px 40px #17243d20}
.orbit-copy {flex:1;min-width:0}.orbit-copy small {color:#b9c9f5;font-size:12px}.orbit-copy strong {display:block;font:800 clamp(26px,5vw,40px) Manrope,Arial;letter-spacing:-1.5px;line-height:1.12;margin:12px 0}.orbit-copy span {color:#d9e4ff;font-size:14px}.orbit-art {width:46%;max-width:280px;flex-shrink:0}.orbit-dot {transform-origin:150px 150px;animation:orbit-spin 18s linear infinite}@keyframes orbit-spin {to{transform:rotate(360deg)}}
@media(prefers-reduced-motion:reduce){.orbit-dot{animation:none}}
.welcome {min-height:58vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:radial-gradient(ellipse at 50% 40%,#354b92,#101a38 72%);border-radius:30px;color:white;padding:24px}.welcome .orbit-art{width:240px;max-width:85%}.welcome strong{font:800 58px Manrope,Arial;letter-spacing:-4px}.welcome span{color:#c5d2f5;font-size:15px;margin-top:8px}
[class*="st-key-nav"] button {border-radius:14px;min-height:48px}.st-key-enter button {min-height:54px;border-radius:16px}.mini-stat{background:white;border:1px solid #e0e6f0;border-radius:18px;padding:16px}.mini-stat small{color:#64748b;font-size:12px}.mini-stat strong{display:block;font:800 25px Manrope,Arial;color:#17243d;margin-top:5px}
@media(max-width:600px){.orbit-panel{padding:18px;min-height:180px;border-radius:22px}.orbit-copy span{font-size:12px}.welcome{min-height:55vh}.welcome strong{font-size:48px}}
</style>""",unsafe_allow_html=True)
TOPICS={
'Türkçe':['Sözcükte anlam','Cümlede anlam','Paragraf','Ses bilgisi','Sözcük türleri','Cümlenin ögeleri','Yazım kuralları','Noktalama','Sözel mantık'],
'Matematik':['Temel kavramlar','Sayılar','Bölünebilme','Rasyonel sayılar','Üslü ve köklü sayılar','Denklemler','Oran ve orantı','Problemler','Sayısal mantık','Geometri'],
'Tarih':['İslamiyet öncesi Türk tarihi','Türk-İslam devletleri','Osmanlı tarihi','Osmanlı kültür ve medeniyeti','Kurtuluş Savaşı','Atatürk ilke ve inkılapları','Çağdaş Türk ve dünya tarihi'],
'Coğrafya':['Coğrafi konum','Yer şekilleri','Dağlar, ovalar ve platolar','Akarsular ve göller','İklim ve bitki örtüsü','Nüfus ve yerleşme','Tarım ve hayvancılık','Madenler ve enerji','Sanayi','Ulaşım ve ticaret','Turizm','Bölgeler coğrafyası'],
'Vatandaşlık':['Hukukun temel kavramları','Anayasa hukuku','Temel hak ve özgürlükler','Yasama','Yürütme','Yargı','İdare hukuku'],
'Güncel bilgiler':['Türkiye ve dünya gündemi','Kültür ve sanat','Bilim ve teknoloji']}
QUESTIONS=[('Coğrafya','Tamamı Türkiye sınırları içinde kalan en uzun akarsu hangisidir?',['Fırat','Dicle','Kızılırmak','Sakarya','Yeşilırmak'],2,'Kızılırmak tamamen Türkiye sınırları içinde akar.'),('Tarih','Türkiye Büyük Millet Meclisi hangi tarihte açılmıştır?',['19 Mayıs 1919','23 Nisan 1920','29 Ekim 1923','30 Ağustos 1922','24 Temmuz 1923'],1,'TBMM 23 Nisan 1920 tarihinde Ankara’da açılmıştır.'),('Matematik','Bir sayının yüzde 25’i 15 ise sayı kaçtır?',['30','45','50','60','75'],3,'15 / 0,25 = 60.'),('Türkçe','Hangisi eş anlamlı bir sözcük çiftidir?',['Gece – gündüz','Az – çok','Uzak – yakın','Kara – siyah','İleri – geri'],3,'Kara ve siyah renk anlamında eş anlamlıdır.'),('Vatandaşlık','Türkiye’de yasama yetkisi hangi organa aittir?',['Danıştay','Yargıtay','TBMM','Sayıştay','Anayasa Mahkemesi'],2,'Anayasa’nın 7. maddesine göre yasama yetkisi TBMM’ye aittir.')]
for k,v in {'page':'Ana sayfa','done':{},'answers':{},'q':0,'exam':0,'notes':{},'wrong':{},'retry':0,'practice':0}.items():
    if k not in st.session_state: st.session_state[k]=v
s=st.session_state
legacy_pages={'Ana Sayfa': 'Ana sayfa', 'Soru Bankası': 'Soru bankası', 'Deneme Sınavları': 'Deneme sınavları', 'Konu Listeleri': 'Konu listeleri', 'Kendi Notlarım': 'Kendi notlarım', 'Yanlış Soru Defterim': 'Yanlış soru defterim', 'Coğrafya Atlası': 'Coğrafya atlası', 'Bilgi Kartları': 'Bilgi kartları', 'Çalışma Takibim': 'Çalışma takibim', 'Akıllı Koç': 'Akıllı koç', 'Akıllı KPSS Koçu': 'Akıllı KPSS koçu', 'Kariyer ve Atama Merkezi': 'Kariyer ve atama merkezi', 'Alım Haberleri': 'Alım haberleri', 'Kişisel Alım Radarı': 'Kişisel alım radarı', 'Tercih Danışmanlığı': 'Tercih danışmanlığı', 'Geçmiş Puanlar': 'Geçmiş puanlar', 'Başvuru Takvimim': 'Başvuru takvimim', 'Kaydedilen İlanlar': 'Kaydedilen ilanlar', 'Atama Radarı': 'Atama radarı', 'Güncel Bilgiler': 'Güncel bilgiler', 'Ön Lisans': 'Ön lisans', 'KİŞİSEL ÇALIŞMA PLANI': 'Kişisel çalışma planı', 'V0.6': 'V0.8'}
if s.page in legacy_pages: s.page=legacy_pages[s.page]
def orbit(value=None):
    label='—' if value is None else f'%{value}'
    arc=0 if value is None else 2.82743*value
    return f'''<svg class="orbit-art" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Örnek cevap başarı göstergesi"><defs><radialGradient id="halo"><stop stop-color="#849cff" stop-opacity=".45"/><stop offset="1" stop-color="#849cff" stop-opacity="0"/></radialGradient></defs><circle cx="150" cy="150" r="145" fill="url(#halo)"/><g fill="none" stroke="#9db4ff" stroke-opacity=".4"><circle cx="150" cy="150" r="125" stroke-dasharray="2 7"/><ellipse cx="150" cy="150" rx="135" ry="65" transform="rotate(-35 150 150)"/><ellipse cx="150" cy="150" rx="135" ry="65" transform="rotate(35 150 150)"/></g><circle cx="150" cy="150" r="45" fill="none" stroke="#7288c9" stroke-width="6"/><circle cx="150" cy="150" r="45" fill="none" stroke="#9af2da" stroke-width="6" stroke-dasharray="{arc} 283" transform="rotate(-90 150 150)" stroke-linecap="round"/><g class="orbit-dot"><circle cx="150" cy="25" r="6" fill="#9af2da"/><circle cx="150" cy="275" r="4" fill="#aebfff"/></g><text x="150" y="157" text-anchor="middle" fill="white" font-size="25" font-weight="700">{label}</text></svg>'''
if not s.get('entered_v08',False):
    st.markdown(f'<div class="welcome">{orbit()}<strong>KPSS.</strong><span>Kişisel eğitim ve kariyer asistanı</span></div>',unsafe_allow_html=True)
    if st.button('Uygulamaya giriş',key='enter',use_container_width=True):
        s.entered_v08=True
        st.rerun()
    st.stop()
st.markdown('<div class="brand"><div class="brand-mark">K</div><div class="brand-name">KPSS.</div></div>',unsafe_allow_html=True)
level=st.selectbox('Sınav seviyen',['Ortaöğretim','Ön lisans','Lisans'],key='level')
def go(page):
    s.page=page
    if page in ['Soru bankası','Deneme sınavları']: s.q=0
    if page=='Deneme sınavları': s.exam+=1
    if page=='Soru bankası': s.practice+=1
    st.rerun()
from datetime import date, datetime, timedelta, timezone
import time
import pandas as pd
TR = timezone(timedelta(hours=3))
def study_day():
    return datetime.now(TR).date()
if "study_logs" not in s: s.study_logs=[]
if "study_timer" not in s: s.study_timer=None
def elapsed(timer):
    return timer["seconds"] + (max(0,time.monotonic()-timer["start"]) if timer["start"] is not None else 0)
def duration(seconds):
    minutes=int(seconds)//60
    return f"{minutes//60} sa. {minutes%60} dk."
def today_seconds():
    return sum(x["seconds"] for x in s.study_logs if x["level"]==level and x["date"]==study_day())
if 'coach_profiles' not in s: s.coach_profiles={}
if 'daily_tasks' not in s: s.daily_tasks={}
profile_coach=s.coach_profiles.get(level,{'target':85,'minutes':45})
def stats():
    result={name:[] for name in TOPICS}
    for key,value in s.answers.items():
        parts=key.split('|')
        if len(parts)==4 and parts[0]==level:
            idx=int(parts[-1])
            if 0<=idx<len(QUESTIONS): result[QUESTIONS[idx][0]].append(bool(value[0]))
    return result
results=stats()
weak=sorted([name for name,vals in results.items() if vals],key=lambda name:sum(results[name])/len(results[name]))
focus=weak[0] if weak else 'Türkçe'
unknown=next((name for name,vals in results.items() if not vals),focus)
nav=[('Ana sayfa','Ana sayfa'),('Eğitim','Dersler'),('Akıllı koç','Akıllı koç'),('Kariyer','Kariyer ve atama merkezi'),('Profil','Profil')]
active_page = s.page if s.page in [p for _,p in nav] else ('Akıllı koç' if s.page=='Bilgi DNA’m' else 'Dersler')
for i,(col,(label,page)) in enumerate(zip(st.columns(5),nav)):
    with col:
        if st.button(label,key=f'nav{i}',type='primary' if active_page==page else 'secondary',use_container_width=True): go(page)
if s.page=='Ana sayfa':
    all_answers=[v for vals in results.values() for v in vals]
    rate=round(100*sum(all_answers)/len(all_answers)) if all_answers else None
    st.markdown(f'<div class="orbit-panel"><div class="orbit-copy"><small>Dijital öğrenci ikizin</small><strong>Hedefin: {profile_coach["target"]} puan</strong><span>{"Henüz cevap verisi yok" if rate is None else "Örnek sorulardaki doğru cevap oranı"}</span></div>{orbit(rate)}</div>',unsafe_allow_html=True)
    a,b=st.columns(2)
    a.metric('Çözülen soru',len(all_answers))
    b.metric('Ölçülen ders',sum(bool(v) for v in results.values()))
    if st.button('Dijital profilimi incele',use_container_width=True): go('Bilgi DNA’m')
    st.subheader('Bugünkü programın')
    tasks=[f'{focus} · {profile_coach["minutes"]//3} dakika konu tekrarı',f'{unknown} · örnek soru çözümü','Yanlış soruları ve notları gözden geçir']
    daykey=(level,date.today().isoformat())
    completed=s.daily_tasks.setdefault(daykey,{})
    for i,task in enumerate(tasks):
        completed[task]=st.checkbox(task,value=completed.get(task,False),key=f'daily_{daykey}_{task}')
    count=sum(bool(completed.get(task)) for task in tasks)
    st.progress(count/len(tasks),text=f'{count}/{len(tasks)} görev tamamlandı')
    st.metric('Bugünkü çalışma süren',duration(today_seconds()))
    if st.button('Kronometreyi aç',use_container_width=True): go('Çalışma takibim')
    if st.button('Soru çözmeye başla',use_container_width=True): go('Soru bankası')
    st.caption('Örnek çalışma planı · Görevleri tamamladıkça işaretle.')
elif s.page=='Dersler':
    st.title('Eğitim')
    modules=[('menu_book','Konu listeleri'),('quiz','Soru bankası'),('edit_note','Kendi notlarım'),('assignment_late','Yanlış soru defterim'),('public','Coğrafya atlası'),('timer','Deneme sınavları'),('style','Bilgi kartları'),('monitoring','Çalışma takibim')]
    for i in range(0,len(modules),2):
        for j,(col,(icon,name)) in enumerate(zip(st.columns(2),modules[i:i+2])):
            with col:
                if st.button(name,icon=f':material/{icon}:',use_container_width=True,key=f'menu{i+j}'): go(name)
elif s.page=='Profil':
    st.title('Çalışma profilim')
    with st.form('coach_profile_'+level):
        target=st.slider('Hedef KPSS puanı',50,100,int(profile_coach['target']))
        minutes=st.slider('Günlük çalışma süresi (dakika)',15,180,int(profile_coach['minutes']),step=15)
        if st.form_submit_button('Profili kaydet'):
            s.coach_profiles[level]={'target':target,'minutes':minutes}; st.rerun()
    st.caption('Profil yalnızca bu oturumda saklanır.')
elif s.page=='Akıllı koç':
    st.title('Akıllı KPSS koçu')
    st.caption('Kural tabanlı Ar-Ge prototipi · Yapay zekâ bağlantısı yok.')
    if not weak: st.info('Henüz performans verin yok. Önce örnek soruları çözerek başlayabilirsin.')
    else:
        st.subheader('Öncelikli çalışma alanın: '+focus)
        vals=results[focus]
        st.write(f'Bu derste {len(vals)} cevapta {sum(vals)} doğru kaydedildi. Daha fazla soru çözerek ölçümü güçlendir.')
    st.write(f'Günlük hedefin: {profile_coach["minutes"]} dakika. Henüz ölçülmemiş ders: {unknown}.' if not results[unknown] else f'Günlük hedefin: {profile_coach["minutes"]} dakika.')
    st.write('Bugün kaydedilen çalışma: '+duration(today_seconds()))
    if st.button('Bilgi DNA’mı incele'): go('Bilgi DNA’m')
    if st.button('Soru çözmeye başla'): go('Soru bankası')
elif s.page=='Bilgi DNA’m':
    st.title('Dijital öğrenci ikizim')
    all_answers=[v for vals in results.values() for v in vals]
    rate=round(100*sum(all_answers)/len(all_answers)) if all_answers else None
    st.markdown(f'<div class="orbit-panel"><div class="orbit-copy"><small>Bilgi DNA’m</small><strong>Öğrenme profilin</strong><span>{len(all_answers)} örnek cevap · Başarı oranı</span></div>{orbit(rate)}</div>',unsafe_allow_html=True)
    st.caption('Gerçek oturum cevaplarından hesaplanan başarı oranı; konu hâkimiyeti veya KPSS puan tahmini değildir.')
    for name,vals in results.items():
        with st.container(border=True):
            st.subheader(name)
            if vals:
                rate=sum(vals)/len(vals)
                st.progress(rate,text=f'%{round(rate*100)} doğru · {len(vals)} cevap')
            else: st.caption('Henüz ölçülmedi')
    if st.button('Koç önerilerime dön'): go('Akıllı koç')
elif s.page=='Kariyer ve atama merkezi':
    st.title('Kariyer ve atama merkezi')
    st.caption('Ar-Ge demosu · Aşağıdaki ilanlar ve puanlar tamamen kurgusaldır.')
    if 'career_saved' not in s: s.career_saved=[]
    if 'career_profile' not in s: s.career_profile={}
    profile=s.career_profile.get(level,{})
    listings=[
        dict(id=1,title='Örnek büro personeli',level='Lisans',city='Ankara',score=70,department='İşletme',kind='Sözleşmeli personel',past=82),
        dict(id=2,title='Örnek memur',level='Ön lisans',city='Elazığ',score=65,department='Tüm bölümler',kind='Memur',past=76),
        dict(id=3,title='Örnek destek personeli',level='Ortaöğretim',city='Malatya',score=60,department='Tüm bölümler',kind='Sözleşmeli personel',past=72),
        dict(id=4,title='Örnek idari personel',level='Lisans',city='İstanbul',score=75,department='Tüm bölümler',kind='Memur',past=85)]
    section=st.radio('Bölüm',['Alım haberleri','Kişisel alım radarı','Tercih danışmanlığı','Geçmiş puanlar','Başvuru takvimim','Kaydedilen ilanlar'],key='career_section')
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
    if section=='Alım haberleri':
        for item in listings: show_listing(item)
        st.markdown('Resmî kaynaklar: [ÖSYM](https://www.osym.gov.tr/) · [Kariyer Kapısı](https://kariyerkapisi.gov.tr/) · [Resmî Gazete](https://www.resmigazete.gov.tr/)')
    elif section=='Kişisel alım radarı':
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
    elif section=='Tercih danışmanlığı':
        st.info('Örnek puan karşılaştırmasıdır; atanma olasılığı veya garantisi değildir.')
        if not profile: st.warning('Önce Kişisel alım radarı bölümünde profilini oluştur.')
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
    elif section=='Geçmiş puanlar':
        for item in listings:
            if item['level']==level: st.metric(item['title']+' · Kurgusal geçmiş puan',item['past'])
    elif section=='Başvuru takvimim':
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
elif s.page=='Konu listeleri':
    st.title('Konu listeleri')
    subject=st.selectbox('Ders seç',list(TOPICS))
    topics=TOPICS[subject]
    for topic in topics:
        key=f'{level}|{subject}|{topic}'
        checked=st.checkbox(topic,value=s.done.get(key,False),key='topic_'+key)
        s.done[key]=checked
    count=sum(s.done.get(f'{level}|{subject}|{t}',False) for t in topics)
    st.progress(count/len(topics),text=f'{count}/{len(topics)} konu tamamlandı')
    st.caption('Örnek konu listesi; resmî müfredat doğrulaması henüz yapılmadı.')
elif s.page in ['Soru bankası','Deneme sınavları']:
    st.title(s.page)
    exam=s.page=='Deneme sınavları'
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
elif s.page=='Kendi notlarım':
    st.title('Kendi notlarım')
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
elif s.page=='Yanlış soru defterim':
    st.title('Yanlış soru defterim')
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
elif s.page=='Coğrafya atlası':
    st.title('Coğrafya atlası')
    places={'Akarsular':{'Kızılırmak':(40.0,34.0,'Tamamı Türkiye sınırları içinde kalan en uzun akarsu.'),'Fırat':(38.7,39.0,'Doğu Anadolu’dan doğar, Basra Körfezi havzasına ulaşır.')},'Göller':{'Van Gölü':(38.6,42.9,'Türkiye’nin yüzölçümü en büyük gölü.'),'Tuz Gölü':(38.75,33.4,'İç Anadolu’da bulunan tuzlu göl.')},'Dağlar':{'Ağrı Dağı':(39.7,44.3,'Türkiye’nin en yüksek dağı.'),'Erciyes':(38.53,35.45,'Kayseri’de bulunan volkanik dağ.')}}
    category=st.selectbox('Harita katmanı',list(places))
    items=places[category]
    st.map([{'lat':v[0],'lon':v[1]} for v in items.values()],zoom=4)
    name=st.selectbox('Coğrafi unsur',list(items))
    st.info(items[name][2])
    st.caption('Yaklaşık konum işaretleri. Fiziki harita ve akarsu çizgileri henüz yok.')
elif s.page=='Bilgi kartları':
    st.title('Bilgi kartları')
    for subject,question,options,correct,explanation in QUESTIONS:
        with st.expander(subject+' · '+question): st.write(options[correct]); st.write(explanation)
elif s.page=='Çalışma takibim':
    st.title('Çalışma takibim')
    timer=s.study_timer
    if timer is None:
        subject=st.selectbox('Ders',list(TOPICS),key='study_subject')
        topic=st.selectbox('Konu',TOPICS[subject],key='study_topic')
        if st.button('Çalışmayı başlat',key='study_start',use_container_width=True):
            s.study_timer=dict(level=level,subject=subject,topic=topic,seconds=0.0,start=time.monotonic())
            st.rerun()
    else:
        st.caption(timer['level']+' · '+timer['subject']+' · '+timer['topic'])
    @st.fragment(run_every=1 if timer and timer['start'] is not None else None)
    def clock():
        current=s.study_timer
        sec=int(elapsed(current)) if current else 0
        display=f'{sec//3600:02d}:{sec//60%60:02d}:{sec%60:02d}'
        status='Çalışılıyor' if current and current['start'] is not None else ('Duraklatıldı' if current else 'Başlamaya hazır')
        st.markdown(f'<div style="background:radial-gradient(ellipse at top,#344c93,#101a38);border-radius:24px;padding:32px 12px;text-align:center;color:white"><div style="font-size:13px;color:#c5d2f5">{status}</div><div style="font:800 clamp(32px,8vw,58px) Manrope,Arial;letter-spacing:-1px;font-variant-numeric:tabular-nums;margin:12px 0">{display}</div><div style="color:#c5d2f5;font-size:13px">Çalışma süresi</div></div>',unsafe_allow_html=True)
        if current:
            a,b=st.columns(2)
            if a.button('Duraklat' if current['start'] is not None else 'Devam et',key='study_pause',use_container_width=True):
                if current['start'] is not None:
                    current['seconds']=elapsed(current); current['start']=None
                else: current['start']=time.monotonic()
                st.rerun()
            if b.button('Bitir ve kaydet',key='study_finish',use_container_width=True):
                seconds=elapsed(current)
                if seconds>=1:
                    s.study_logs.append(dict(level=current['level'],subject=current['subject'],topic=current['topic'],seconds=seconds,date=study_day()))
                s.study_timer=None
                st.rerun()
    clock()
    logs=[x for x in s.study_logs if x['level']==level]
    today=study_day(); monday=today-timedelta(days=today.weekday())
    week=[x for x in logs if monday<=x['date']<=today]
    a,b=st.columns(2)
    a.metric('Bugün',duration(today_seconds()))
    b.metric('Bu hafta',duration(sum(x['seconds'] for x in week)))
    target=profile_coach['minutes']*60
    st.progress(min(1.0,today_seconds()/target),text=f'Günlük hedef: {profile_coach["minutes"]} dakika')
    st.subheader('Haftalık çalışma grafiği')
    days=[monday+timedelta(days=i) for i in range(7)]
    frame=pd.DataFrame({'Gün':[d.strftime('%d.%m') for d in days],'Dakika':[round(sum(x['seconds'] for x in week if x['date']==d)/60,2) for d in days]})
    st.bar_chart(frame,x='Gün',y='Dakika',color='#5264df')
    st.subheader('Derslere göre çalışma süresi')
    if week:
        frame=pd.DataFrame({'Ders':list(TOPICS),'Dakika':[round(sum(x['seconds'] for x in week if x['subject']==name)/60,2) for name in TOPICS]})
        st.bar_chart(frame,x='Ders',y='Dakika',color='#23b5a0')
    else: st.info('Grafikler ilk çalışma kaydından sonra dolacak.')
    with st.expander('Çalışma geçmişim'):
        for item in reversed(logs):
            st.write(f"{item['date']:%d.%m.%Y} · {item['subject']} · {item['topic']} · {int(item['seconds'])//60} dk. {int(item['seconds'])%60} sn.")
        if not logs: st.caption('Henüz çalışma kaydı yok.')
    st.caption('Süreler bitirip kaydettiğinde grafiklere eklenir. Kayıt tarihi bitiş günüdür. Kronometre diğer sayfalarda da süre sayar; oturum kapanırsa kayıtlar kaybolabilir.')
    st.subheader('Soru ve konu istatistikleri')
    answers=[v for k,v in s.answers.items() if k.startswith(level+'|')]
    correct=sum(v[0] for v in answers)
    a,b=st.columns(2); a.metric('Doğru',correct); b.metric('Yanlış',len(answers)-correct)
    st.metric('Tamamlanan konu',sum(v for k,v in s.done.items() if k.startswith(level+'|')))
    if answers: st.progress(correct/len(answers),text=f'Başarı: %{round(100*correct/len(answers))}')
    st.caption('Veriler yalnızca mevcut oturumda tutulur.')
st.divider()
st.caption('V0.10 · Ar-Ge sürümü · Veriler oturumluk')

# Aslan ve canlı koçluk: bağımsız demo bileşenleri.
st.markdown("""<style>
.block-container {padding-bottom:120px}
.st-key-aslan_float {position:fixed;right:22px;bottom:22px;width:210px;z-index:999;}
.st-key-aslan_float button {background:#17243d!important;color:white!important;border-radius:22px!important;box-shadow:0 8px 30px #17243d33;min-height:58px;}
.st-key-aslan_float button p {color:white!important;font-size:13px;}
.st-key-aslan_float svg {display:block;margin-left:auto;filter:drop-shadow(0 5px 8px #17243d22)}
@media(max-width:600px){.st-key-aslan_float{right:12px;bottom:12px;width:185px}}
</style>""",unsafe_allow_html=True)
if 'aslan_messages' not in s: s.aslan_messages=[]
if 'premium_demo' not in s: s.premium_demo=False
if 'support_open' not in s: s.support_open=False
if 'aslan_open' not in s: s.aslan_open=False
if 'support_requests' not in s: s.support_requests=[]
with st.container(key='aslan_float'):
    st.markdown('<svg width="76" height="76" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-label="Aslan maskotu"><circle cx="50" cy="50" r="47" fill="#fff5df"/><path d="M50 7 Q65 2 72 18 Q94 16 91 38 Q105 52 88 65 Q90 86 68 85 Q50 103 32 85 Q10 86 12 65 Q-5 52 9 38 Q6 16 28 18 Q35 2 50 7" fill="#b97627"/><circle cx="28" cy="32" r="12" fill="#efb65d"/><circle cx="72" cy="32" r="12" fill="#efb65d"/><ellipse cx="50" cy="53" rx="30" ry="32" fill="#f6c878"/><ellipse cx="50" cy="65" rx="20" ry="14" fill="#fff1cf"/><circle cx="38" cy="48" r="4" fill="#17243d"/><circle cx="62" cy="48" r="4" fill="#17243d"/><path d="M44 59 Q50 55 56 59 L50 65Z" fill="#17243d"/><path d="M50 65 Q44 73 39 68 M50 65 Q56 73 61 68" fill="none" stroke="#17243d" stroke-width="2" stroke-linecap="round"/><path d="M30 81 Q50 90 70 81 L65 93 L35 93Z" fill="#5264df"/></svg>',unsafe_allow_html=True)
    if st.button('Nasıl yardımcı olabilirim?',key='aslan_toggle',use_container_width=True):
        s.aslan_open=True
        st.rerun()

def aslan_reply(prompt):
    q=prompt.casefold()
    if s.page in ['Soru bankası','Deneme sınavları'] and s.q<len(QUESTIONS) and any(w in q for w in ['soru','çöz','açıkla','ipucu']):
        _,question,options,correct,explanation=QUESTIONS[s.q]
        return 'Bu sorunun çözümü: '+explanation+' Doğru seçenek: '+options[correct]+'.'
    for _,question,options,correct,explanation in QUESTIONS:
        if question.casefold().rstrip('?') in q:
            return explanation+' Doğru cevap: '+options[correct]+'.'
    if 'tbmm' in q and ('açıl' in q or 'tarih' in q): return 'TBMM, 23 Nisan 1920 tarihinde Ankara’da açılmıştır.'
    if 'kızılırmak' in q: return 'Kızılırmak, tamamı Türkiye sınırları içinde kalan en uzun akarsudur.'
    if 'yasama' in q: return 'Anayasa’nın 7. maddesine göre yasama yetkisi TBMM’ye aittir.'
    if 'çalış' in q or 'program' in q: return f'Bugün {duration(today_seconds())} çalıştın. Günlük hedefin {profile_coach["minutes"]} dakika. Öncelikli tekrar alanın: {focus}.'
    return 'Bu demo sürümünde yalnızca örnek soruları, bazı temel KPSS bilgilerini ve çalışma verilerini açıklayabiliyorum. Genel yapay zekâ bağlantısı henüz kurulmadı.'

@st.dialog('Aslan · Eğitim asistanı')
def aslan_dialog():
    st.caption('Demo asistan · Hazır bilgiler ve basit kurallar kullanır.')
    if st.button('Canlı koçluk',key='aslan_support'):
        s.aslan_open=False; s.support_open=True; st.rerun()
    if st.button('Bu soruyu açıkla',key='aslan_explain',disabled=not(s.page in ['Soru bankası','Deneme sınavları'] and s.q<len(QUESTIONS))):
        s.aslan_messages.extend([('user','Bu soruyu açıkla'),('assistant',aslan_reply('Bu soruyu açıkla'))])
    for role,msg in s.aslan_messages[-20:]:
        with st.chat_message(role): st.write(msg)
    with st.form('aslan_chat',clear_on_submit=True):
        prompt=st.text_input('Aslan’a sor')
        if st.form_submit_button('Gönder') and prompt.strip():
            s.aslan_messages.extend([('user',prompt.strip()),('assistant',aslan_reply(prompt.strip()))]); st.rerun()
    if st.button('Kapat',key='aslan_close'):
        s.aslan_open=False; st.rerun()

@st.dialog('Canlı koçluk · Premium')
def support_dialog():
    st.caption('Temsili koçlar ve müsaitlik durumları · Gerçek görüşme yapılmaz.')
    s.premium_demo=st.checkbox('Premium demo erişimini aç',value=s.premium_demo,key='premium_switch')
    for name,area,online in [('Matematik koçu','Matematik ve geometri',True),('Genel kültür koçu','Tarih ve coğrafya',True),('Tercih danışmanı','Atama ve tercih süreçleri',False)]:
        with st.container(border=True):
            st.markdown('**'+name+'**')
            st.caption(area+' · '+('🟢 Müsait (demo)' if online else 'Çevrimdışı (demo)'))
            if st.button('Bağlan' if online else 'Randevu talep et',key='support_'+name,disabled=not s.premium_demo,use_container_width=True):
                s.support_requests.append(name)
                st.success('Demo talebi kaydedildi. Gerçek koça iletilmedi.')
    if st.button('Kapat',key='support_close'):
        s.support_open=False; st.rerun()

if st.button('Canlı destek · Premium',key='live_support',use_container_width=True):
    s.support_open=True; s.aslan_open=False; st.rerun()
if s.support_open: support_dialog()
elif s.aslan_open: aslan_dialog()

