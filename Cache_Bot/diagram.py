Başla
|
└─ Ana Program (Main.py)
   |
   └─ Cache_Bot Oluştur
      |
      └─ Bot Ayarları Yap
      |  |
      |  └─ Komut Öneki Belirle
      |  └─ Yetkilendirme Ayarları
      |  └─ Uzantıları Yükle
      |     |
      |     └─ Uzantıları Otomatik Yükle
      |        |
      |        └─ Her Bir Uzantıyı Yükle
      |           |
      |           └─ Başarıyla Yükleme Durumunda
      |           └─ Hata Durumunda Hata Mesajı Göster
      |
      └─ Bot'u Çalıştır
         |
         └─ Token Kontrol Et
         |  |
         |  └─ Token Var İse
         |  |  |
         |  |  └─ Bot'u Çalıştır
         |  |  └─ "Logged In" Mesajını Göster
         |  |
         |  └─ Token Yok İse
         |     |
         |     └─ "Log In Failure, check location of token." Mesajını Göster
         |
         └─ Bot'u Sonlandır
|
└─ CSV_Channel Cog
|  |
|  └─ Belirli Kanaldaki Mesajları CSV'ye Kaydet
|     |
|     └─ Gerekli Kolonları Oluştur
|     └─ Kanaldaki Mesajları Al
|     |  |
|     |  └─ Intro Belirtilmiş İse
|     |  |  |
|     |  |  └─ Geçerli Girişler ve Mesajlar İçin
|     |  |     |
|     |  |     └─ Mesajları İşle ve CSV'ye Kaydet
|     |  |
|     |  └─ Intro Belirtilmemiş İse
|     |     |
|     |     └─ Tüm Mesajlar İçin
|     |        |
|     |        └─ Mesajları İşle ve CSV'ye Kaydet
|     |
|     └─ İşlemi Tamamla ve Bitir
|
└─ SingleCSV Cog
   |
   └─ Tüm Sunucudaki Mesajları Tek Bir CSV'ye Kaydet
      |
      └─ Gerekli Kolonları Oluştur
      └─ Tüm Kanalları Al
      |  |
      |  └─ Kanal Türü Text İse
      |     |
      |     └─ Kanaldaki Mesajları Al
      |        |
      |        └─ Mesajları İşle ve CSV'ye Kaydet
      |
      └─ İşlemi Tamamla ve Bitir
|
Bitir




