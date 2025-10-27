-- CSV MODUNA GEÇELİM
.mode csv

-- 2. TAM YOLU FORWARDSLASH İLE YAZDIM ÇÜNKÜ SADECE DOSYA ADINI YAZINCA AÇMADI
.import "C:/Users/Dilanur/Desktop/sl dosyasi/netflix_titles.csv" netflix_titles

-- 1. EN YENİ 5 FİLM
SELECT title, type, release_year
FROM netflix_titles
WHERE type = 'Movie' --filmleri getir
ORDER BY release_year DESC --yılları yeniden eskiye sırala
LIMIT 5; -- 5 tane yeterli

-- 2. EN FAZLA İÇERİK ÜRETEN ÜLKE
SELECT country, count(*) as sayi 
FROM netflix_titles
GROUP BY country -- ülkelere göre gruplandır
ORDER BY sayi DESC -- sırayla sayılarını yaz ne kadar içerik var
LIMIT 5;

-- 3. EN UZUN FİLM
SELECT title,type,duration 
FROM netflix_titles
WHERE type = 'Movie'
ORDER BY duration DESC --büyükten küçüğe sirala
LIMIT 5;