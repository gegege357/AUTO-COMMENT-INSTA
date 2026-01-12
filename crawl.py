from instalooter.looters import ProfileLooter
import pandas as pd
import time

# ==============================
# KONFIGURASI
# ==============================
USERNAME = 'geabutttt'   # akun harus PUBLIC
OUTPUT_CSV = 'hasil_crawling_instagram.csv'

# ==============================
# INISIALISASI
# ==============================
looter = ProfileLooter(USERNAME)

data = []
print("[+] Mulai crawling ...")

# ==============================
# CRAWLING POST
# ==============================
for media in looter.medias():
    try:
        info = looter.get_post_info(media['shortcode'])

        post_id = info.get('id')
        shortcode = info.get('shortcode')
        owner = info.get('owner', {}).get('username')
        total_like = info.get('edge_media_preview_like', {}).get('count', 0)
        total_comment = info.get('edge_media_to_parent_comment', {}).get('count', 0)

        comments = info.get('edge_media_to_parent_comment', {}).get('edges', [])

        if comments:
            for c in comments:
                comm_text = c.get('node', {}).get('text')
                comm_user = c.get('node', {}).get('owner', {}).get('username')

                data.append([
                    post_id,
                    shortcode,
                    owner,
                    total_like,
                    total_comment,
                    comm_user,
                    comm_text
                ])
        else:
            data.append([
                post_id,
                shortcode,
                owner,
                total_like,
                total_comment,
                None,
                None
            ])

        time.sleep(1)  # ⛔ penting biar tidak kena rate limit

    except Exception as e:
        print(f"[!] Error pada post {media['shortcode']}: {e}")
        continue

print("[+] Crawling selesai!")

# ==============================
# DATAFRAME
# ==============================
df = pd.DataFrame(data, columns=[
    'id_post',
    'shortcode',
    'pemilik_post',
    'total_like',
    'total_komentar',
    'username_komentar',
    'teks_komentar'
])

# ==============================
# SIMPAN KE CSV
# ==============================
df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')

print(f"[+] Data berhasil disimpan ke {OUTPUT_CSV}")
print(df.head())
