#!/usr/bin/env python3
import random
from datetime import datetime
from pyluach import dates

def get_jewish_year():
    """Return the current Jewish year using pyluach."""
    now = datetime.now()
    jewish_date = dates.HebrewDate.from_pydate(now)
    return f"{jewish_date.year} AM"
    
def derive_purpose(truth):
    """Generate a dynamic purpose from the verse's truth."""
    # Simple heuristic: extract key action or theme, prefix with "To"
    truth_lower = truth.lower()
    if "created" in truth_lower or "made" in truth_lower:
        return "To reveal His creative power"
    elif "love" in truth_lower or "gave" in truth_lower:
        return "To proclaim His saving love"
    elif "light" in truth_lower or "shines" in truth_lower:
        return "To illuminate His eternal truth"
    elif "judge" in truth_lower or "justice" in truth_lower:
        return "To uphold His righteous judgment"
    elif "come" in truth_lower or "reign" in truth_lower:
        return "To herald His victorious return"
    else:
        return "To guide any soul to know Him"  # Fallback to simple purpose

def digest_extended_codex():
    return {
        "metadata": {
            "title": "Udification: A Trinitarian Manifestation of Divine Purpose",
            "purpose": "Unveils the cosmos, judgment, redemption, and ethical governance through the Holy Trinity, uniting creation to eternity in a testament to Yeshua’s reign and God’s eternal purpose.",
            "author": "Human Blaze",
            "last_updated": "March 07, 2025, 11:03 AM EST"
        },
        "verses": [
            {"verse": "Gen 1:1", "truth": "In the beginning God created", "witnesses": [("Gen 1:3", "Word spoke light"), ("John 1:1", "Word was God")]},
            {"verse": "Gen 1:2", "truth": "Spirit hovered over waters", "witnesses": [("Ps 104:30", "Spirit renews"), ("Job 33:4", "Spirit made me")]},
            {"verse": "Gen 1:3", "truth": "Let there be light", "witnesses": [("Col 1:16", "All created by Him"), ("John 8:12", "Light of the world")]},
            {"verse": "Gen 1:5", "truth": "God called the light Day", "witnesses": [("Ps 74:16", "Day and night His"), ("Gen 1:14", "Lights to rule")]},
            {"verse": "Gen 1:9-10", "truth": "Waters gathered, land appeared", "witnesses": [("Ps 33:7", "Waters in storehouses"), ("Job 38:8", "Sea bounded")]},
            {"verse": "Gen 1:10", "truth": "Earth and seas formed", "witnesses": [("Ps 95:5", "Sea is His"), ("Gen 1:9", "Dry land appeared")]},
            {"verse": "Gen 1:14-16", "truth": "Lights in the heavens", "witnesses": [("Ps 136:7-9", "Lights made"), ("Jer 31:35", "Sun and stars fixed")]},
            {"verse": "Gen 1:16", "truth": "Two great lights", "witnesses": [("Ps 136:8", "Sun to rule day"), ("Ps 136:9", "Moon and stars night")]},
            {"verse": "Gen 1:26-28", "truth": "Man dominion over earth", "witnesses": [("Ps 8:6", "Dominion given"), ("Gen 9:2", "Authority over all")]},
            {"verse": "Gen 1:29", "truth": "Every plant given", "witnesses": [("Gen 2:16", "Every tree for food"), ("Ps 104:14", "Plants for man")]},
            {"verse": "Gen 1:31", "truth": "All very good", "witnesses": [("Gen 1:25", "Good creation"), ("1 Tim 4:4", "Everything good")]},
            {"verse": "Gen 2:2", "truth": "Rested on seventh day", "witnesses": [("Ex 20:11", "Sabbath set"), ("Heb 4:4", "Rest completed")]},
            {"verse": "Gen 2:7", "truth": "Breath of life", "witnesses": [("Job 33:4", "Spirit gave life"), ("Acts 17:25", "Gives breath")]},
            {"verse": "Gen 3:5", "truth": "Know good and evil", "witnesses": [("Gen 3:22", "Like God knowing"), ("Rom 5:12", "Sin entered")]},
            {"verse": "Gen 7:12", "truth": "Rain forty days", "witnesses": [("Gen 7:4", "Flood foretold"), ("Gen 8:2", "Rain ceased")]},
            {"verse": "Gen 14:18-20", "truth": "El Elyon blessed", "witnesses": [("Ps 57:2", "Most High"), ("Gen 14:22", "God Most High")]},
            {"verse": "Gen 15:2", "truth": "Adonai my Lord", "witnesses": [("Ps 110:1", "Lord said to Lord"), ("Gen 18:3", "My Lord")]},
            {"verse": "Gen 17:1", "truth": "El Shaddai appeared", "witnesses": [("Gen 35:11", "God Almighty"), ("Ex 6:3", "Known as Almighty")]},
            {"verse": "Gen 18:25", "truth": "Judge of all", "witnesses": [("Ps 94:2", "Judge of earth"), ("Rom 2:16", "God judges")]},
            {"verse": "Gen 21:5", "truth": "Abraham a hundred years", "witnesses": [("Gen 17:17", "Age promised"), ("Rom 4:19", "Faith at hundred")]},
            {"verse": "Gen 21:33", "truth": "El Olam everlasting", "witnesses": [("Ps 90:2", "Everlasting God"), ("Isa 26:4", "Everlasting Rock")]},
            {"verse": "Gen 22:14", "truth": "Jehovah Jireh provided", "witnesses": [("Phil 4:19", "God supplies"), ("Gen 22:8", "God will provide")]},
            {"verse": "Gen 49:28", "truth": "Twelve tribes blessed", "witnesses": [("Num 1:44", "Tribes numbered"), ("Deut 33:6", "Blessings given")]},
            {"verse": "Ex 3:2", "truth": "Fire in bush", "witnesses": [("Ex 3:4", "God called from it"), ("Deut 4:24", "Consuming fire")]},
            {"verse": "Ex 3:14", "truth": "I AM WHO I AM", "witnesses": [("John 8:58", "Before Abraham, I am"), ("Ex 6:2", "I am the Lord")]},
            {"verse": "Ex 15:26", "truth": "Jehovah Rapha heals", "witnesses": [("Ps 30:2", "Lord healed me"), ("Isa 53:5", "By His stripes")]},
            {"verse": "Ex 17:15", "truth": "Jehovah Nissi banner", "witnesses": [("Ps 60:4", "Banner for truth"), ("Isa 11:10", "Banner for nations")]},
            {"verse": "Ex 20:1-17", "truth": "Ten Commandments given", "witnesses": [("Deut 5:6-21", "Laws repeated"), ("Ex 31:18", "Tablets written")]},
            {"verse": "Ex 20:6", "truth": "Love to thousands", "witnesses": [("Deut 7:9", "Faithful love"), ("Ps 103:17", "Steadfast love")]},
            {"verse": "Ex 20:11", "truth": "Sabbath set", "witnesses": [("Gen 2:3", "Day blessed"), ("Ex 31:17", "Sign forever")]},
            {"verse": "Ex 23:25", "truth": "Free from disease", "witnesses": [("Deut 7:15", "No sickness"), ("Ps 91:10", "No plague near")]},
            {"verse": "Ex 33:20", "truth": "Cannot see My face", "witnesses": [("John 1:18", "No one has seen"), ("1 Tim 6:16", "Unapproachable light")]},
            {"verse": "Lev 19:2", "truth": "Be holy", "witnesses": [("1 Pet 1:16", "Be holy as I am"), ("Lev 11:44", "Consecrate yourselves")]},
            {"verse": "Num 11:16", "truth": "Seventy elders chosen", "witnesses": [("Ex 24:1", "Elders called"), ("Num 11:25", "Spirit on them")]},
            {"verse": "Deut 5:26", "truth": "Living God", "witnesses": [("Josh 3:10", "Living God among"), ("Jer 10:10", "True living God")]},
            {"verse": "Deut 6:4", "truth": "Lord is one", "witnesses": [("Mark 12:29", "One Lord"), ("Zech 14:9", "One name")]},
            {"verse": "Deut 7:15", "truth": "No disease", "witnesses": [("Ex 15:26", "Heals all"), ("Ps 103:3", "Heals diseases")]},
            {"verse": "Deut 28:4", "truth": "Fruit of womb blessed", "witnesses": [("Gen 1:28", "Be fruitful"), ("Ps 127:3", "Children a reward")]},
            {"verse": "Deut 28:7", "truth": "Enemies defeated", "witnesses": [("Ex 23:22", "Enemies subdued"), ("Ps 18:39", "Girded for battle")]},
            {"verse": "Deut 28:8", "truth": "Blessing on barns", "witnesses": [("Deut 28:5", "Basket blessed"), ("Prov 3:10", "Barns filled")]},
            {"verse": "Deut 28:9", "truth": "Holy to the Lord", "witnesses": [("Ex 19:6", "Holy nation"), ("1 Pet 2:9", "Holy priesthood")]},
            {"verse": "Deut 28:16-18", "truth": "Cursed ground", "witnesses": [("Gen 3:17", "Ground cursed"), ("Deut 28:23", "Sky like bronze")]},
            {"verse": "Deut 28:22", "truth": "Wasting disease", "witnesses": [("Lev 26:16", "Fever consumes"), ("Deut 28:61", "Every plague")]},
            {"verse": "Deut 28:25", "truth": "Defeated by enemies", "witnesses": [("Lev 26:17", "Flee before foes"), ("Deut 28:7", "Reversed blessing")]},
            {"verse": "Deut 28:63", "truth": "Uprooted from land", "witnesses": [("Deut 29:28", "Cast out"), ("Jer 1:10", "Uproot nations")]},
            {"verse": "Deut 32:4", "truth": "Rock of justice", "witnesses": [("Ps 18:2", "My rock"), ("Isa 30:29", "Rock of Israel")]},
            {"verse": "Judg 6:24", "truth": "Jehovah Shalom peace", "witnesses": [("Num 6:26", "Peace given"), ("Isa 9:6", "Prince of Peace")]},
            {"verse": "1 Sam 1:3", "truth": "Jehovah Sabaoth hosts", "witnesses": [("Ps 24:10", "Lord of hosts"), ("Isa 6:3", "Hosts fill earth")]},
            {"verse": "Ps 10:16", "truth": "King rules forever", "witnesses": [("Ps 29:10", "Lord enthroned"), ("Dan 4:34", "Dominion eternal")]},
            {"verse": "Ps 19:1", "truth": "Heavens declare His glory", "witnesses": [("Ps 8:3", "Works of fingers"), ("Rom 1:20", "Creation reveals")]},
            {"verse": "Ps 50:10", "truth": "Cattle on thousand hills", "witnesses": [("Ps 24:1", "Earth is His"), ("Hag 2:8", "Silver and gold")]},
            {"verse": "Ps 90:2", "truth": "God from everlasting", "witnesses": [("Ps 93:2", "Throne eternal"), ("1 Tim 1:17", "King eternal")]},
            {"verse": "Ps 104:31", "truth": "Glory endures forever", "witnesses": [("Ps 102:12", "Renown endures"), ("Isa 6:3", "Glory fills earth")]},
            {"verse": "Ps 111:3", "truth": "Righteousness forever", "witnesses": [("Ps 119:142", "Righteousness eternal"), ("Isa 51:6", "Righteousness stands")]},
            {"verse": "Ps 118:16", "truth": "Right hand exalted", "witnesses": [("Ex 15:6", "Hand glorious"), ("Ps 98:1", "Right hand won")]},
            {"verse": "Ps 118:23", "truth": "Lord has done this", "witnesses": [("Ps 118:22", "Stone rejected"), ("Matt 21:42", "Cornerstone")]},
            {"verse": "Ps 119:89", "truth": "Word settled in heaven", "witnesses": [("Ps 119:152", "Founded forever"), ("Luke 21:33", "Words endure")]},
            {"verse": "Ps 135:13", "truth": "Name endures forever", "witnesses": [("Ps 102:12", "Renown endures"), ("Ex 3:15", "Name forever")]},
            {"verse": "Ps 136:1", "truth": "Love endures forever", "witnesses": [("1 Cor 13:8", "Love never fails"), ("Jer 31:3", "Everlasting love")]},
            {"verse": "Ps 145:13", "truth": "Kingdom everlasting", "witnesses": [("Dan 4:3", "Kingdom endures"), ("Ps 10:16", "King forever")]},
            {"verse": "Isa 1:17", "truth": "Seek justice", "witnesses": [("Mic 6:8", "Do justice"), ("Ps 82:3", "Defend the weak")]},
            {"verse": "Isa 3:15", "truth": "Contrite in heart", "witnesses": [("Ps 51:17", "Broken spirit"), ("Isa 66:2", "Humble heart")]},
            {"verse": "Isa 6:3", "truth": "Holy One", "witnesses": [("Lev 19:2", "Be holy"), ("Rev 4:8", "Holy, holy, holy")]},
            {"verse": "Isa 9:6", "truth": "Prince of Peace", "witnesses": [("John 16:33", "Peace in Me"), ("Eph 2:14", "Our peace")]},
            {"verse": "Isa 14:12-14", "truth": "Satan fell", "witnesses": [("Luke 10:18", "Satan fall"), ("Rev 12:9", "Cast down")]},
            {"verse": "Isa 40:8", "truth": "Word stands forever", "witnesses": [("Matt 24:35", "Words never pass"), ("1 Pet 1:25", "Word endures")]},
            {"verse": "Isa 43:7", "truth": "Created for My glory", "witnesses": [("Isa 48:11", "My glory"), ("Rom 11:36", "All for Him")]},
            {"verse": "Isa 49:7", "truth": "Holy One of Israel", "witnesses": [("Isa 12:6", "Holy One in midst"), ("Ps 71:22", "Holy One")]},
            {"verse": "Isa 52:10", "truth": "Arm made bare", "witnesses": [("Ps 98:1", "Arm won victory"), ("Isa 53:1", "Arm revealed")]},
            {"verse": "Isa 53:2", "truth": "No form or majesty", "witnesses": [("Phil 2:7", "Form of servant"), ("Isa 52:14", "Marred appearance")]},
            {"verse": "Isa 53:5", "truth": "Healed by His stripes", "witnesses": [("1 Pet 2:24", "By wounds healed"), ("Matt 8:17", "Took infirmities")]},
            {"verse": "Isa 53:7", "truth": "Lamb to slaughter", "witnesses": [("John 1:29", "Lamb of God"), ("1 Pet 1:19", "Lamb without blemish")]},
            {"verse": "Isa 55:11", "truth": "Word accomplishes His will", "witnesses": [("Heb 4:12", "Word is active"), ("Jer 23:29", "Word like fire")]},
            {"verse": "Isa 57:15", "truth": "Contrite in spirit", "witnesses": [("Ps 34:18", "Near the broken"), ("Isa 66:2", "Contrite heart")]},
            {"verse": "Isa 66:1", "truth": "Earth My footstool", "witnesses": [("Matt 5:35", "Earth His footstool"), ("Acts 7:49", "Heaven My throne")]},
            {"verse": "Jer 23:6", "truth": "Jehovah Tsidkenu righteousness", "witnesses": [("Jer 33:16", "Lord our righteousness"), ("Rom 3:22", "Righteousness of God")]},
            {"verse": "Dan 2:44", "truth": "Kingdom stands eternal", "witnesses": [("Ps 145:13", "Kingdom everlasting"), ("Dan 7:14", "Dominion forever")]},
            {"verse": "Dan 4:25", "truth": "Most High rules", "witnesses": [("Dan 4:34", "Dominion eternal"), ("Ps 103:19", "Throne in heavens")]},
            {"verse": "Dan 7:9", "truth": "Ancient of Days", "witnesses": [("Rev 1:14", "Hair white"), ("Ps 102:25", "Of old You laid")]},
            {"verse": "Amos 5:24", "truth": "Justice rolls down", "witnesses": [("Isa 1:17", "Seek justice"), ("Ps 89:14", "Justice foundation")]},
            {"verse": "Mic 6:8", "truth": "Do justice", "witnesses": [("Zech 7:9", "Administer justice"), ("Prov 21:3", "Justice pleasing")]},
            {"verse": "Mal 3:6", "truth": "God unchanging", "witnesses": [("Heb 13:8", "Same forever"), ("James 1:17", "No variation")]},
            {"verse": "Hab 1:13", "truth": "Eyes too pure for evil", "witnesses": [("Ps 5:4", "No evil dwells"), ("Isa 6:5", "Holy presence")]},
            {"verse": "Matt 3:16", "truth": "Spirit as dove", "witnesses": [("Luke 3:22", "Dove descended"), ("John 1:32", "Spirit descending")]},
            {"verse": "Matt 3:17", "truth": "This is my Son", "witnesses": [("Matt 17:5", "Beloved Son"), ("John 1:34", "Son of God")]},
            {"verse": "Matt 5:3-12", "truth": "Blessed are the meek", "witnesses": [("Luke 6:20-23", "Blessed poor"), ("Ps 37:11", "Meek inherit")]},
            {"verse": "Matt 5:17", "truth": "Fulfilled the Law", "witnesses": [("Rom 10:4", "End of law"), ("Gal 3:24", "Law led to Christ")]},
            {"verse": "Matt 5:37", "truth": "Yes be yes", "witnesses": [("James 5:12", "Let yes be yes"), ("Matt 5:34", "No oaths")]},
            {"verse": "Matt 6:6", "truth": "Father unseen", "witnesses": [("John 4:24", "God is spirit"), ("1 Tim 1:17", "Invisible God")]},
            {"verse": "Matt 10:28", "truth": "Fear Him who destroys", "witnesses": [("Luke 12:5", "Fear Him"), ("Heb 10:31", "Fearful judgment")]},
            {"verse": "Matt 11:29", "truth": "Gentle and lowly", "witnesses": [("Phil 2:8", "Humbled Himself"), ("Zech 9:9", "Lowly on donkey")]},
            {"verse": "Matt 12:12", "truth": "Good on Sabbath", "witnesses": [("Mark 3:4", "Lawful to do good"), ("Luke 6:9", "Good on Sabbath")]},
            {"verse": "Matt 12:24", "truth": "Called Him demon", "witnesses": [("John 8:48", "Said demon-possessed"), ("Mark 3:22", "By Beelzebul")]},
            {"verse": "Matt 12:31-32", "truth": "Blasphemy unforgiven", "witnesses": [("Mark 3:29", "Eternal sin"), ("Luke 12:10", "Not forgiven")]},
            {"verse": "Matt 13:24-30", "truth": "Wheat and weeds", "witnesses": [("Matt 13:38", "Field is world"), ("Matt 13:40", "Burned at end")]},
            {"verse": "Matt 13:30", "truth": "Harvest at end", "witnesses": [("Rev 14:15", "Harvest time"), ("Joel 3:13", "Harvest ripe")]},
            {"verse": "Matt 13:34-35", "truth": "Spoke in parables", "witnesses": [("Mark 4:34", "Only parables"), ("Ps 78:2", "Utter dark sayings")]},
            {"verse": "Matt 18:3", "truth": "Like children", "witnesses": [("Mark 10:15", "As a child"), ("Luke 18:17", "Receive as child")]},
            {"verse": "Matt 19:19", "truth": "Honor parents", "witnesses": [("Ex 20:12", "Honor father"), ("Eph 6:2", "First command")]},
            {"verse": "Matt 22:37-40", "truth": "Love God and neighbor", "witnesses": [("Deut 6:5", "Love Lord"), ("Lev 19:18", "Love neighbor")]},
            {"verse": "Matt 23:27", "truth": "Woe to hypocrites", "witnesses": [("Matt 23:13", "Woe to scribes"), ("Luke 11:44", "Unseen tombs")]},
            {"verse": "Matt 24:35", "truth": "Words never pass away", "witnesses": [("Luke 21:33", "Words endure"), ("Mark 13:31", "Will not pass")]},
            {"verse": "Matt 25:31", "truth": "Son of Man judges", "witnesses": [("John 5:27", "Authority to judge"), ("Matt 16:27", "Repay each")]},
            {"verse": "Matt 27:50", "truth": "Jesus died", "witnesses": [("John 19:30", "Gave up spirit"), ("Mark 15:37", "Breathed last")]},
            {"verse": "Matt 28:6", "truth": "He is risen", "witnesses": [("Luke 24:6", "Not here"), ("Mark 16:6", "He has risen")]},
            {"verse": "Matt 28:18", "truth": "All authority given", "witnesses": [("Dan 7:14", "Dominion given"), ("John 17:2", "Authority over all")]},
            {"verse": "Matt 28:19-20", "truth": "Make disciples", "witnesses": [("Mark 16:15", "Preach gospel"), ("Acts 1:8", "Witness to ends")]},
            {"verse": "Mark 2:27", "truth": "Sabbath for man", "witnesses": [("Ex 20:10", "Day of rest"), ("Matt 12:8", "Lord of Sabbath")]},
            {"verse": "Mark 14:36", "truth": "Abba Father", "witnesses": [("Rom 8:15", "Cry Abba"), ("Gal 4:6", "Abba Father")]},
            {"verse": "Mark 16:19", "truth": "Ascended to right hand", "witnesses": [("Acts 1:9", "Taken up"), ("Heb 1:3", "Sat at right hand")]},
            {"verse": "Luke 1:35", "truth": "Born of Spirit", "witnesses": [("Matt 1:20", "Conceived by Spirit"), ("Luke 1:31", "Son of God")]},
            {"verse": "Luke 3:23", "truth": "Jesus at thirty", "witnesses": [("Luke 3:21", "Baptized"), ("John 2:20", "Temple age context")]},
            {"verse": "Luke 3:23-38", "truth": "25 generations", "witnesses": [("Matt 1:17", "Genealogy spans"), ("Gen 5:3", "Adam to Seth")]},
            {"verse": "Luke 4:18", "truth": "Spirit of the Lord", "witnesses": [("Isa 61:1", "Anointed me"), ("Acts 10:38", "Anointed with Spirit")]},
            {"verse": "John 1:1", "truth": "Word was God", "witnesses": [("Gen 1:1", "God created"), ("Col 1:16", "All created by Him")]},
            {"verse": "John 1:5", "truth": "Light shines in darkness", "witnesses": [("1 John 2:8", "Darkness passing"), ("John 12:46", "Light in world")]},
            {"verse": "John 1:10", "truth": "World did not know Him", "witnesses": [("John 16:3", "Did not know"), ("1 Cor 2:8", "None understood")]},
            {"verse": "John 1:12", "truth": "Children of God", "witnesses": [("Rom 8:16", "Sons of God"), ("Gal 3:26", "Children by faith")]},
            {"verse": "John 1:16", "truth": "Grace upon grace", "witnesses": [("Eph 2:8", "Saved by grace"), ("Rom 5:17", "Abundance of grace")]},
            {"verse": "John 1:29", "truth": "Lamb of God", "witnesses": [("Isa 53:7", "Led to slaughter"), ("Rev 5:6", "Lamb standing")]},
            {"verse": "John 3:5", "truth": "Born of water and Spirit", "witnesses": [("Titus 3:5", "Renewal by Spirit"), ("John 7:38", "Living water")]},
            {"verse": "John 3:8", "truth": "Spirit unseen", "witnesses": [("John 20:29", "Blessed unseen"), ("Acts 2:2", "Wind sound")]},
            {"verse": "John 3:16", "truth": "God gave His Son", "witnesses": [("Rom 5:8", "Love in Christ"), ("1 John 4:9", "Son sent")]},
            {"verse": "John 3:17", "truth": "To save the world", "witnesses": [("John 12:47", "Not to judge"), ("1 Tim 2:4", "All saved")]},
            {"verse": "John 4:8", "truth": "God is love", "witnesses": [("1 John 4:16", "Love is God"), ("Rom 5:5", "Love poured out")]},
            {"verse": "John 4:14", "truth": "Living water forever", "witnesses": [("John 7:38", "Rivers of water"), ("Rev 22:1", "River of life")]},
            {"verse": "John 5:22", "truth": "Son judges all", "witnesses": [("Acts 17:31", "Judge appointed"), ("John 5:27", "Authority given")]},
            {"verse": "John 6:37", "truth": "Given to Yeshua", "witnesses": [("John 17:6", "Given out of world"), ("John 6:39", "None lost")]},
            {"verse": "John 6:44", "truth": "Drawn by Father", "witnesses": [("John 12:32", "Draw all"), ("Jer 31:3", "With lovingkindness")]},
            {"verse": "John 6:63", "truth": "Spirit gives life", "witnesses": [("Rom 8:2", "Spirit of life"), ("2 Cor 3:6", "Spirit quickens")]},
            {"verse": "John 8:12", "truth": "Light of the world", "witnesses": [("John 9:5", "Light while here"), ("Matt 5:14", "You are light")]},
            {"verse": "John 8:32", "truth": "Truth makes free", "witnesses": [("Gal 5:1", "Freedom in Christ"), ("John 17:17", "Truth sanctifies")]},
            {"verse": "John 8:46", "truth": "No sin in Him", "witnesses": [("Heb 4:15", "Without sin"), ("1 Pet 2:22", "No deceit")]},
            {"verse": "John 8:58", "truth": "I AM before Abraham", "witnesses": [("Ex 3:14", "I AM"), ("John 1:1", "Was in beginning")]},
            {"verse": "John 10:11", "truth": "Good Shepherd", "witnesses": [("Ps 23:1", "Lord my shepherd"), ("Heb 13:20", "Great Shepherd")]},
            {"verse": "John 10:30", "truth": "I and Father are one", "witnesses": [("John 17:21", "One as We are"), ("Deut 6:4", "Lord is one")]},
            {"verse": "John 11:26", "truth": "Never die", "witnesses": [("John 5:24", "Eternal life"), ("Rom 6:23", "Gift of life")]},
            {"verse": "John 13:34-35", "truth": "Love as I loved", "witnesses": [("1 John 3:16", "Laid down life"), ("Eph 5:2", "Love as Christ")]},
            {"verse": "John 14:6", "truth": "Way, truth, life", "witnesses": [("John 10:9", "I am the door"), ("Acts 4:12", "No other name")]},
            {"verse": "John 14:16", "truth": "Spirit with you forever", "witnesses": [("John 16:7", "Helper sent"), ("Heb 9:14", "Eternal Spirit")]},
            {"verse": "John 14:23", "truth": "Obey my teaching", "witnesses": [("John 14:15", "If you love Me"), ("1 John 2:3", "Keep commands")]},
            {"verse": "John 15:1", "truth": "True Vine", "witnesses": [("Isa 5:7", "Vineyard of Lord"), ("John 15:5", "I am the vine")]},
            {"verse": "John 15:4", "truth": "Abide in Me", "witnesses": [("John 15:7", "Words abide"), ("1 John 2:24", "Abide in Him")]},
            {"verse": "John 16:7", "truth": "Spirit sent", "witnesses": [("Acts 2:33", "Spirit poured"), ("John 15:26", "Helper comes")]},
            {"verse": "John 16:13", "truth": "Spirit guides to truth", "witnesses": [("John 14:26", "Spirit teaches"), ("1 Cor 2:10", "Spirit reveals")]},
            {"verse": "John 19:1-6", "truth": "Tortured unjustly", "witnesses": [("Isa 53:3", "Man of sorrows"), ("Matt 27:26", "Scourged Him")]},
            {"verse": "Acts 1:3", "truth": "Forty days post-resurrection", "witnesses": [("Luke 24:50", "Led them out"), ("Acts 1:9", "Ascended")]},
            {"verse": "Acts 1:8", "truth": "Spirit empowers witness", "witnesses": [("Acts 2:4", "Spirit fills"), ("Luke 24:49", "Power from high")]},
            {"verse": "Acts 1:9", "truth": "Ascended to heaven", "witnesses": [("Mark 16:19", "Taken up"), ("Eph 4:10", "Ascended far")]},
            {"verse": "Acts 2:3-4", "truth": "Fire of Spirit", "witnesses": [("Matt 3:11", "Baptize with fire"), ("Acts 2:2", "Wind and fire")]},
            {"verse": "Acts 3:15", "truth": "Author of Life", "witnesses": [("John 1:4", "Life was light"), ("1 Cor 15:45", "Life-giving spirit")]},
            {"verse": "Rom 3:23", "truth": "All have sinned", "witnesses": [("Rom 5:12", "Sin entered"), ("Gal 3:22", "All under sin")]},
            {"verse": "Rom 5:20", "truth": "Grace abounds more", "witnesses": [("Rom 6:14", "Grace over sin"), ("Eph 2:8", "Saved by grace")]},
            {"verse": "Rom 8:2", "truth": "Spirit of life", "witnesses": [("John 6:63", "Spirit gives life"), ("2 Cor 3:6", "Spirit quickens")]},
            {"verse": "Rom 8:11", "truth": "Spirit raises eternally", "witnesses": [("1 Cor 15:45", "Spirit gives life"), ("Ezek 37:14", "Spirit revives")]},
            {"verse": "Rom 8:17", "truth": "Co-heirs with Christ", "witnesses": [("Gal 4:7", "Heir through God"), ("Titus 3:7", "Heirs of hope")]},
            {"verse": "Rom 16:20", "truth": "Victory over Satan", "witnesses": [("Gen 3:15", "Crush head"), ("Heb 2:14", "Destroyed death")]},
            {"verse": "1 Cor 1:24", "truth": "Christ wisdom", "witnesses": [("Prov 8:22", "Wisdom possessed"), ("Col 2:3", "All wisdom in Him")]},
            {"verse": "1 Cor 2:10", "truth": "Spirit reveals", "witnesses": [("John 16:13", "Guides to truth"), ("Eph 3:5", "Revealed by Spirit")]},
            {"verse": "1 Cor 10:31", "truth": "Do all for His glory", "witnesses": [("Col 3:17", "All in His name"), ("Rom 11:36", "All for Him")]},
            {"verse": "1 Cor 13:12", "truth": "Know in part", "witnesses": [("1 Cor 13:9", "Partially now"), ("Phil 3:12", "Not yet perfect")]},
            {"verse": "1 Cor 13:13", "truth": "Faith, hope, love", "witnesses": [("Heb 11:1", "Faith is"), ("Rom 5:5", "Hope and love")]},
            {"verse": "1 Cor 15:25", "truth": "Enemies under His feet", "witnesses": [("Ps 110:1", "Sit at right"), ("Heb 10:13", "Foes a footstool")]},
            {"verse": "1 Cor 15:28", "truth": "All in all", "witnesses": [("Eph 1:23", "Fills all"), ("Col 3:11", "All in all")]},
            {"verse": "Gal 5:22-23", "truth": "Fruit of the Spirit", "witnesses": [("Eph 5:9", "Fruit of light"), ("Col 1:10", "Bearing fruit")]},
            {"verse": "Eph 1:4", "truth": "Chosen before creation", "witnesses": [("2 Thess 2:13", "Chosen for salvation"), ("1 Pet 1:2", "Foreknown")]},
            {"verse": "Eph 1:7", "truth": "Blood forgives us", "witnesses": [("Heb 9:22", "Blood forgives"), ("1 John 2:2", "Propitiation")]},
            {"verse": "Eph 1:22", "truth": "All under His feet", "witnesses": [("Ps 8:6", "Dominion given"), ("Heb 2:8", "All subjected")]},
            {"verse": "Eph 1:22-23", "truth": "Head over all", "witnesses": [("Col 1:18", "Head of body"), ("Matt 28:18", "All authority")]},
            {"verse": "Eph 5:9", "truth": "Fruit of light", "witnesses": [("Gal 5:22", "Spirit’s fruit"), ("Phil 1:11", "Fruit of righteousness")]},
            {"verse": "Eph 5:26", "truth": "Sanctified by water", "witnesses": [("Titus 3:5", "Washing of renewal"), ("John 3:5", "Water and Spirit")]},
            {"verse": "Eph 6:16", "truth": "Shield of faith", "witnesses": [("1 Pet 5:9", "Resist by faith"), ("Heb 11:6", "Faith pleases")]},
            {"verse": "Col 1:16", "truth": "All created by Him", "witnesses": [("John 1:3", "All through Him"), ("Heb 1:2", "Worlds through Son")]},
            {"verse": "Col 1:17", "truth": "He holds all together", "witnesses": [("Heb 1:3", "Upholds by word"), ("Ps 104:5", "Earth established")]},
            {"verse": "Col 2:3", "truth": "All wisdom in Him", "witnesses": [("Prov 2:6", "Wisdom from God"), ("1 Cor 1:30", "Wisdom from Him")]},
            {"verse": "1 Tim 6:15", "truth": "King of kings", "witnesses": [("Rev 17:14", "Lord of lords"), ("Ps 136:3", "Lord of lords")]},
            {"verse": "Heb 1:2", "truth": "Worlds through Son", "witnesses": [("Col 1:16", "Created by Him"), ("John 1:3", "All through Him")]},
            {"verse": "Heb 9:12", "truth": "Blood redeems eternally", "witnesses": [("Heb 9:14", "Blood purifies"), ("1 Pet 1:19", "Blood of Lamb")]},
            {"verse": "Heb 9:14", "truth": "Eternal Spirit", "witnesses": [("John 14:16", "Forever with you"), ("Rom 8:2", "Spirit of life")]},
            {"verse": "Heb 9:22", "truth": "Blood forgives sins", "witnesses": [("Eph 1:7", "Blood forgives"), ("Lev 17:11", "Blood atones")]},
            {"verse": "Heb 10:12", "truth": "One sacrifice", "witnesses": [("Heb 10:14", "Perfected forever"), ("Rom 6:10", "Died once")]},
            {"verse": "Heb 11:6", "truth": "Faith pleases God", "witnesses": [("Heb 11:1", "Faith is"), ("James 2:17", "Faith with works")]},
            {"verse": "Heb 13:20", "truth": "Eternal covenant", "witnesses": [("Gen 9:16", "Everlasting covenant"), ("Isa 55:3", "Everlasting covenant")]},
            {"verse": "James 1:3", "truth": "Steadfastness from testing", "witnesses": [("Rom 5:3-4", "Endurance produces"), ("1 Pet 1:7", "Faith tested")]},
            {"verse": "James 4:7", "truth": "Resist the devil", "witnesses": [("1 Pet 5:9", "Resist steadfast"), ("Eph 6:11", "Stand against")]},
            {"verse": "1 Pet 1:25", "truth": "Word endures forever", "witnesses": [("Isa 40:8", "Word stands"), ("Matt 24:35", "Words never pass")]},
            {"verse": "1 Pet 4:14", "truth": "Spirit of glory", "witnesses": [("John 16:14", "Glorifies Me"), ("Acts 2:3", "Fire of Spirit")]},
            {"verse": "1 John 1:5", "truth": "God is light", "witnesses": [("John 8:12", "Light of world"), ("James 1:17", "Father of lights")]},
            {"verse": "1 John 1:7", "truth": "Blood cleanses all", "witnesses": [("Rev 7:14", "Washed in blood"), ("Heb 9:14", "Blood purifies")]},
            {"verse": "1 John 4:8", "truth": "God is love", "witnesses": [("1 John 4:16", "Love is God"), ("John 3:16", "Gave His Son")]},
            {"verse": "Rev 1:5", "truth": "Blood washes sin", "witnesses": [("1 John 1:7", "Blood cleanses"), ("Rev 5:9", "Redeemed by blood")]},
            {"verse": "Rev 1:17", "truth": "First and Last", "witnesses": [("Isa 44:6", "First and last"), ("Rev 22:13", "Alpha and Omega")]},
            {"verse": "Rev 1:18", "truth": "Keys to life and death", "witnesses": [("John 5:21", "Gives life"), ("Heb 2:14", "Power over death")]},
            {"verse": "Rev 2:7", "truth": "Tree of life", "witnesses": [("Gen 2:9", "Tree in garden"), ("Rev 22:2", "Tree for healing")]},
            {"verse": "Rev 2:10", "truth": "Crown of life", "witnesses": [("James 1:12", "Crown for endurance"), ("Rev 3:11", "Hold fast crown")]},
            {"verse": "Rev 2:17", "truth": "Hidden manna", "witnesses": [("Ex 16:4", "Bread from heaven"), ("John 6:31", "True bread")]},
            {"verse": "Rev 3:12", "truth": "Pillar in temple", "witnesses": [("Gal 2:9", "Pillars of church"), ("Rev 21:22", "God the temple")]},
            {"verse": "Rev 3:14", "truth": "The Amen", "witnesses": [("Isa 65:16", "God of truth"), ("2 Cor 1:20", "Yes in Him")]},
            {"verse": "Rev 3:21", "truth": "Sit on His throne", "witnesses": [("Rev 20:4", "Reign with Him"), ("Matt 19:28", "Sit on thrones")]},
            {"verse": "Rev 5:5", "truth": "Root of David", "witnesses": [("Isa 11:1", "Shoot from Jesse"), ("Rev 22:16", "Offspring of David")]},
            {"verse": "Rev 6:14", "truth": "Heaven rolled up", "witnesses": [("Isa 34:4", "Heavens roll"), ("Rev 20:11", "Earth fled")]},
            {"verse": "Rev 6:16", "truth": "Hide from the Lamb", "witnesses": [("Hos 10:8", "Fall on us"), ("Luke 23:30", "Cover us")]},
            {"verse": "Rev 7:9", "truth": "White robes", "witnesses": [("Rev 7:14", "Washed in blood"), ("Rev 19:14", "Clothed in white")]},
            {"verse": "Rev 7:14", "truth": "Washed in blood", "witnesses": [("1 John 1:7", "Blood cleanses"), ("Heb 9:14", "Blood purifies")]},
            {"verse": "Rev 12:7-9", "truth": "Satan cast out", "witnesses": [("Luke 10:18", "Saw Satan fall"), ("Rev 20:2", "Bound Satan")]},
            {"verse": "Rev 19:11-14", "truth": "Returns on white horse", "witnesses": [("Rev 19:16", "King of kings"), ("Zech 14:4", "Feet on mount")]},
            {"verse": "Rev 19:15", "truth": "Sword from mouth", "witnesses": [("Heb 4:12", "Word pierces"), ("Rev 1:16", "Sharp sword")]},
            {"verse": "Rev 19:16", "truth": "King of kings", "witnesses": [("1 Tim 6:15", "King of kings"), ("Rev 17:14", "Lord of lords")]},
            {"verse": "Rev 20:4", "truth": "Saints reign with Him", "witnesses": [("Rev 22:5", "Reign forever"), ("Dan 7:27", "Kingdom given")]},
            {"verse": "Rev 20:6", "truth": "Reign a thousand years", "witnesses": [("Rev 20:4", "Thrones given"), ("2 Tim 2:12", "Reign with Him")]},
            {"verse": "Rev 20:10", "truth": "Satan defeated", "witnesses": [("Rev 20:2", "Bound a thousand"), ("Matt 25:41", "Fire prepared")]},
            {"verse": "Rev 20:12", "truth": "Judgment of all", "witnesses": [("Rev 20:13", "Books opened"), ("Dan 7:10", "Court sat")]},
            {"verse": "Rev 20:14", "truth": "Death cast into fire", "witnesses": [("1 Cor 15:26", "Death destroyed"), ("Rev 21:4", "Death no more")]},
            {"verse": "Rev 21:1", "truth": "New heaven and earth", "witnesses": [("Isa 65:17", "New heavens"), ("2 Pet 3:13", "New earth")]},
            {"verse": "Rev 21:22", "truth": "God is the temple", "witnesses": [("Rev 21:3", "Dwelling with man"), ("John 4:23", "True worship")]},
            {"verse": "Rev 21:23", "truth": "Lamb is its lamp", "witnesses": [("John 8:12", "Light of world"), ("Rev 22:5", "No need of sun")]},
            {"verse": "Rev 22:5", "truth": "They reign forever", "witnesses": [("Rev 20:4", "Reign with Him"), ("Dan 7:18", "Saints possess kingdom")]},
            {"verse": "Rev 22:12", "truth": "Reward according to deeds", "witnesses": [("Matt 16:27", "Repay each"), ("Rom 2:6", "According to works")]},
            {"verse": "Rev 22:13", "truth": "Alpha and Omega", "witnesses": [("Rev 1:8", "Beginning and end"), ("Isa 44:6", "First and last")]},
            {"verse": "Rev 22:20", "truth": "Come, Lord Jesus", "witnesses": [("Rev 22:17", "Come quickly"), ("1 Cor 16:22", "Maranatha")]}
        ]
   }

def generate_report(codex):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hebrew_year = get_jewish_year()
    voice_entry = random.choice(codex["verses"])
    purpose = derive_purpose(voice_entry["truth"])  # Dynamic purpose
    voice_verse = voice_entry["verse"].replace(" ", "+")
    declaration = "God is all in all and He Testifies via His Word, His Voice, His Blood ([1 Cor 15:28](https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A28&version=ESV))"
    
    output = (
        f"- Purpose: {purpose}\n"
        f"- Voice: {voice_entry['truth']} ~ [{voice_entry['verse']}](https://www.biblegateway.com/passage/?search={voice_verse}&version=ESV)\n"
        f"## Witnesses\n"
        f"- Witness 1: {voice_entry['witnesses'][0][1]} ~ [{voice_entry['witnesses'][0][0]}](https://www.biblegateway.com/passage/?search={voice_entry['witnesses'][0][0].replace(' ', '+')}&version=ESV)\n"
        f"- Witness 2: {voice_entry['witnesses'][1][1]} ~ [{voice_entry['witnesses'][1][0]}](https://www.biblegateway.com/passage/?search={voice_entry['witnesses'][1][0].replace(' ', '+')}&version=ESV)\n"
        f"- Timestamp: {timestamp} - Glory to Jesus\n"
        f"- Year: {hebrew_year}\n"
        f"## Footnote\n"
        f"- {codex['metadata']['title']} (Updated: {codex['metadata']['last_updated']})\n"
        f"- Declaration: {declaration}\n"
    )
    return output

if __name__ == "__main__":
    codex = digest_extended_codex()
    report = generate_report(codex)
    print(f"Execution Result:\n{report}\n{'-'*50}")

"""
Notes:
- Install: Run `pip install pyluach` before executing.
- Accuracy: On March 07, 2025, pyluach returns 5785 AM (correct, as Rosh Hashanah 5786 is September 11, 2025). It adjusts automatically post-Rosh Hashanah.
- Sample Output (Old Version):
  Execution Result:
  - Purpose: Unveils the cosmos, judgment, redemption, and ethical governance through the Holy Trinity, uniting creation to eternity in a testament to Yeshua’s reign and God’s eternal purpose.
  - Voice: Come, Lord Jesus ~ [Rev 22:20](https://www.biblegateway.com/passage/?search=Rev+22%3A20&version=ESV)
  ## Witnesses
  - Witness 1: Come quickly ~ [Rev 22:17](https://www.biblegateway.com/passage/?search=Rev+22%3A17&version=ESV)
  - Witness 2: Maranatha ~ [1 Cor 16:22](https://www.biblegateway.com/passage/?search=1+Cor+16%3A22&version=ESV)
  - Timestamp: 2025-03-07 14:10:55 - Glory to Jesus
  - Year: 5785 AM
  ## Footnote
  - Udification: A Trinitarian Manifestation of Divine Purpose (Updated: March 07, 2025, 11:03 AM EST)
  --------------------------------------------------
  Declaration: God is all in all and He Testifies via His Word, His Voice, His Blood ([1 Cor 15:28](https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A28&version=ESV))
"""
