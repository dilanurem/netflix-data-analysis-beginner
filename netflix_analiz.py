import pandas as pd

df = pd.read_csv('netflix_titles.csv')

#ilk 5 satırı gösterelim bakalım çalışıyor mu
print("ilk 5 kayıt: ")
print(df.head())

#toplam kaç film ve dizi var?
if 'type' in df.columns: #kolonlarda tip var ise
    print("\n--- FİLM VE TV ŞOVU DAĞILIMI ---")
    print(df['type'].value_counts())
else:
    print("type sütunu bulunamadı. Bulunan sütunlar : ")
    print(df.columns.tolist())

#hangi ülkeler en fazla içeriğe sahip?
print("\n**** EN FAZLA İÇERİK ÜRETEN ÜLKELER ****")
if 'country' in df.columns:
    print(df['country'].value_counts().head(10)) #ilk 10 ülkeyi alsın
else:
    print("'country' sütunu bulunamadı. ")

#en yeni içerikler
print("\n---- EN YENİ 5 İÇERİK ----")
if 'release_year' in df.columns:
    # veriyi yeniden eskiye göre sırala
    yeniIcerikler = df.sort_values('release_year', ascending=False)
    # ilk 5 kaydı alalım
    yeniIcerikler = yeniIcerikler.head(5)
    # sadece titl,type ve release_year sütunlarını göstersin
    print(yeniIcerikler[['title','type','release_year']])
else: 
    print("'release_year' sütunu bulunamadı.")