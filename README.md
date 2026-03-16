# 💰 FinTrack

FinTrack, kişisel gelir ve giderlerinizi terminal üzerinden kolayca takip etmenizi sağlayan, hafif ve kullanıcı dostu bir Python komut satırı (CLI) uygulamasıdır.

## 🚀 Özellikler

- **Gelir Ekleme:** Kazançlarınızı açıklama, miktar ve kategori ile detaylıca kaydedin.
- **Gider Ekleme:** Harcamalarınızı kolayca sisteme girin ve paranızın nereye gittiğini bilin.
- **İşlem Geçmişi:** Tüm gelir ve giderlerinizi okunması kolay, düzenli bir tablo formatında görüntüleyin.
- **Finansal Özet:** Toplam gelir, toplam gider ve net bakiyenizi anında analiz edin.
- **Veri Kalıcılığı:** Tüm kayıtlarınız `data.json` dosyasında güvenle saklanır; uygulamayı kapatsanız bile verileriniz her zaman güvendedir.

## 📋 Gereksinimler

- **Python 3.x**
- Herhangi bir ek kütüphane kurulumu gerektirmez (Sadece Python'un standart kütüphanelerini kullanır).

## 🛠️ Kurulum & Kullanım

1. Proje dizinine terminalinizden (veya Komut İstemcisi/PowerShell) gidin.
   ```bash
   cd "C:\Users\Kullanici\Masaüstü\FinTrack"
   ```
2. Uygulamayı çalıştırın:
   ```bash
   python FinTrack.py
   ```

## 🎮 Menü Seçenekleri

Uygulamayı çalıştırdığınızda aşağıdaki kullanıcı dostu menü ile karşılacaksınız:

- `1. Add Income`  : Yeni bir gelir kaydı oluşturur.
- `2. Add Expense` : Yeni bir gider kaydı oluşturur.
- `3. List All`    : Tüm finansal hareketleri tablo şeklinde listeler.
- `4. Summary`     : Toplam gelir, gider ve net bakiye analizini gösterir.
- `5. Exit`        : Uygulamadan güvenli bir şekilde çıkar.

## 📂 Dosya Yapısı

- `FinTrack.py` : Uygulamanın çekirdek kodunu barındıran çalıştırılabilir dosya.
- `data.json`   : Uygulamanın verileri kaydettiği yerel veritabanı dosyası (İşlem yaptıkça otomatik oluşturulur veya güncellenir).