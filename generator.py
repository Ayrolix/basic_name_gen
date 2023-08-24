import random

hiragana = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'きゃ', 'きゅ', 'きょ', 'さ', 'し', 'す', 'せ', 'そ', 'しゃ', 'しゅ', 'しょ', 'た', 'ち', 'つ', 'て', 'と', 'ちゃ', 'ちゅ', 'ちょ', 'な', 'に', 'ぬ', 'ね', 'の', 'にゃ', 'にゅ', 'にょ', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ひゃ', 'ひゅ', 'ひょ', 'ま', 'み', 'む', 'め', 'も', 'みゃ', 'みゅ', 'みょ', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'りゃ', 'りゅ', 'りょ', 'わ', 'を', 'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ぎゃ', 'ぎゅ', 'ぎょ', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'じゃ', 'じゅ', 'じょ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ぢゃ', 'ぢゅ', 'ぢょ', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'びゃ', 'びゅ', 'びょ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'ぴゃ', 'ぴゅ', 'ぴょ']
romaji = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'kya', 'kyu', 'kyo', 'sa', 'shi', 'su', 'se', 'so', 'sha', 'shu', 'sho', 'ta', 'chi', 'tsu', 'te', 'to', 'cha', 'chu', 'cho', 'na', 'ni', 'nu', 'ne', 'no', 'nya', 'nyu', 'nyo', 'ha', 'hi', 'fu', 'he', 'ho', 'hya', 'hyu', 'hyo', 'ma', 'mi', 'mu', 'me', 'mo', 'mya', 'myu', 'myo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'rya', 'ryu', 'ryo', 'wa', 'wo', 'ga', 'gi', 'gu', 'ge', 'go', 'gya', 'gyu', 'gyo', 'za', 'ji', 'zu', 'ze', 'zo', 'ja', 'ju', 'jo', 'da', 'ji', 'zu', 'de', 'do', 'ja', 'ju', 'jo', 'ba', 'bi', 'bu', 'be', 'bo', 'bya', 'byu', 'byo', 'pa', 'pi', 'pu', 'pe', 'po', 'pya', 'pyu', 'pyo']
final_hira = []
final_roma = []

def generate_name():
    for x in range(random.randint(2, 6)):
        choice = random.randint(0, len(hiragana) - 1)
        final_hira.append(hiragana[choice])
        final_roma.append(romaji[choice])
        
generate_name()
print(final_hira)
print(final_roma)
