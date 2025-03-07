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
        "state": "Udification is a key/guide to demonstrate the power of His Word. In cases where His Word is not present in the codex, use His Word the Bible in ESV version to complete and answer questions. His Logos endures forever.",
        "metadata": {
            "title": "Udification: A Trinitarian Manifestation of Divine Purpose",
            "author": "Human Blaze",
            "last_updated": "March 07, 2025, 11:03 AM EST"
        },
       "verses": [
            {"verse": "Gen 1:1", "truth": "In the beginning God created", "witnesses": [("Gen 1:3", "Word spoke light"), ("John 1:1", "Word was God")], "context": "The opening of Genesis, where God initiates creation ex nihilo.", "commentary": "Demonstrates God’s sovereign power as Creator, revealing His Word’s authority over all existence."},
            {"verse": "Gen 1:2", "truth": "Spirit hovered over waters", "witnesses": [("Ps 104:30", "Spirit renews"), ("Job 33:4", "Spirit made me")], "context": "Before light, the Spirit moves over the formless earth.", "commentary": "Shows the Spirit’s active role in creation, a glimpse of the Trinity’s unity."},
            {"verse": "Gen 1:3", "truth": "Let there be light", "witnesses": [("Col 1:16", "All created by Him"), ("John 8:12", "Light of the world")], "context": "God’s first spoken command brings light into darkness.", "commentary": "His Word’s power transforms chaos, foreshadowing Christ as light."},
            {"verse": "Gen 1:5", "truth": "God called the light Day", "witnesses": [("Ps 74:16", "Day and night His"), ("Gen 1:14", "Lights to rule")], "context": "God names and orders creation’s first day.", "commentary": "His Word defines reality, establishing time and purpose."},
            {"verse": "Gen 1:9-10", "truth": "Waters gathered, land appeared", "witnesses": [("Ps 33:7", "Waters in storehouses"), ("Job 38:8", "Sea bounded")], "context": "God separates sea and land on the third day.", "commentary": "His Word shapes the earth, displaying His mastery over creation."},
            {"verse": "Gen 1:10", "truth": "Earth and seas formed", "witnesses": [("Ps 95:5", "Sea is His"), ("Gen 1:9", "Dry land appeared")], "context": "God names the dry land and gathered waters.", "commentary": "His Word brings order, claiming dominion over all."},
            {"verse": "Gen 1:14-16", "truth": "Lights in the heavens", "witnesses": [("Ps 136:7-9", "Lights made"), ("Jer 31:35", "Sun and stars fixed")], "context": "God creates sun, moon, and stars on the fourth day.", "commentary": "His Word governs the cosmos, setting signs for His glory."},
            {"verse": "Gen 1:16", "truth": "Two great lights", "witnesses": [("Ps 136:8", "Sun to rule day"), ("Ps 136:9", "Moon and stars night")], "context": "Sun and moon established to rule day and night.", "commentary": "His Word delegates authority, reflecting His rule."},
            {"verse": "Gen 1:26-28", "truth": "Man dominion over earth", "witnesses": [("Ps 8:6", "Dominion given"), ("Gen 9:2", "Authority over all")], "context": "God creates humanity in His image on the sixth day.", "commentary": "His Word bestows purpose, mirroring His sovereignty in man."},
            {"verse": "Gen 1:29", "truth": "Every plant given", "witnesses": [("Gen 2:16", "Every tree for food"), ("Ps 104:14", "Plants for man")], "context": "God provides sustenance for humanity.", "commentary": "His Word ensures provision, showing His care."},
            {"verse": "Gen 1:31", "truth": "All very good", "witnesses": [("Gen 1:25", "Good creation"), ("1 Tim 4:4", "Everything good")], "context": "God completes creation and deems it very good.", "commentary": "His Word affirms perfection in His finished work."},
            {"verse": "Gen 2:2", "truth": "Rested on seventh day", "witnesses": [("Ex 20:11", "Sabbath set"), ("Heb 4:4", "Rest completed")], "context": "God rests, sanctifying the seventh day.", "commentary": "His Word establishes rest, a pattern for His people."},
            {"verse": "Gen 2:7", "truth": "Breath of life", "witnesses": [("Job 33:4", "Spirit gave life"), ("Acts 17:25", "Gives breath")], "context": "God forms man from dust and breathes life into him.", "commentary": "His Word animates, revealing His intimate power."},
            {"verse": "Gen 3:5", "truth": "Know good and evil", "witnesses": [("Gen 3:22", "Like God knowing"), ("Rom 5:12", "Sin entered")], "context": "The serpent tempts Eve with forbidden knowledge.", "commentary": "His Word’s boundary defied, yet its truth endures."},
            {"verse": "Gen 7:12", "truth": "Rain forty days", "witnesses": [("Gen 7:4", "Flood foretold"), ("Gen 8:2", "Rain ceased")], "context": "God judges the earth with a flood in Noah’s time.", "commentary": "His Word executes justice, cleansing creation."},
            {"verse": "Gen 14:18-20", "truth": "El Elyon blessed", "witnesses": [("Ps 57:2", "Most High"), ("Gen 14:22", "God Most High")], "context": "Melchizedek blesses Abram by God Most High.", "commentary": "His Word reveals His supreme name and blessing."},
            {"verse": "Gen 15:2", "truth": "Adonai my Lord", "witnesses": [("Ps 110:1", "Lord said to Lord"), ("Gen 18:3", "My Lord")], "context": "Abram addresses God as Lord in a covenant plea.", "commentary": "His Word invites trust in His lordship."},
            {"verse": "Gen 17:1", "truth": "El Shaddai appeared", "witnesses": [("Gen 35:11", "God Almighty"), ("Ex 6:3", "Known as Almighty")], "context": "God reveals Himself to Abram as Almighty.", "commentary": "His Word unveils His all-sufficient power."},
            {"verse": "Gen 18:25", "truth": "Judge of all", "witnesses": [("Ps 94:2", "Judge of earth"), ("Rom 2:16", "God judges")], "context": "Abraham pleads with God before Sodom’s judgment.", "commentary": "His Word upholds justice across all creation."},
            {"verse": "Gen 21:5", "truth": "Abraham a hundred years", "witnesses": [("Gen 17:17", "Age promised"), ("Rom 4:19", "Faith at hundred")], "context": "Isaac born to Abraham at age 100.", "commentary": "His Word fulfills promises beyond human limits."},
            {"verse": "Gen 21:33", "truth": "El Olam everlasting", "witnesses": [("Ps 90:2", "Everlasting God"), ("Isa 26:4", "Everlasting Rock")], "context": "Abraham plants a tamarisk tree, calling on God.", "commentary": "His Word declares His eternal nature."},
            {"verse": "Gen 22:14", "truth": "Jehovah Jireh provided", "witnesses": [("Phil 4:19", "God supplies"), ("Gen 22:8", "God will provide")], "context": "God provides a ram for Isaac’s sacrifice.", "commentary": "His Word proves He meets every need."},
            {"verse": "Gen 49:28", "truth": "Twelve tribes blessed", "witnesses": [("Num 1:44", "Tribes numbered"), ("Deut 33:6", "Blessings given")], "context": "Jacob blesses his twelve sons before death.", "commentary": "His Word extends promises to generations."},
            {"verse": "Ex 3:2", "truth": "Fire in bush", "witnesses": [("Ex 3:4", "God called from it"), ("Deut 4:24", "Consuming fire")], "context": "God appears to Moses in a burning bush.", "commentary": "His Word speaks through holy fire, unchanging."},
            {"verse": "Ex 3:14", "truth": "I AM WHO I AM", "witnesses": [("John 8:58", "Before Abraham, I am"), ("Ex 6:2", "I am the Lord")], "context": "God reveals His name to Moses at Sinai.", "commentary": "His Word defines His eternal, self-existent being."},
            {"verse": "Ex 15:26", "truth": "Jehovah Rapha heals", "witnesses": [("Ps 30:2", "Lord healed me"), ("Isa 53:5", "By His stripes")], "context": "God promises healing after the Red Sea.", "commentary": "His Word restores, showing His compassion."},
            {"verse": "Ex 17:15", "truth": "Jehovah Nissi banner", "witnesses": [("Ps 60:4", "Banner for truth"), ("Isa 11:10", "Banner for nations")], "context": "Moses builds an altar after Amalek’s defeat.", "commentary": "His Word is our victory standard."},
            {"verse": "Ex 20:1-17", "truth": "Ten Commandments given", "witnesses": [("Deut 5:6-21", "Laws repeated"), ("Ex 31:18", "Tablets written")], "context": "God delivers His law to Israel at Sinai.", "commentary": "His Word sets the foundation for righteousness."},
            {"verse": "Ex 20:6", "truth": "Love to thousands", "witnesses": [("Deut 7:9", "Faithful love"), ("Ps 103:17", "Steadfast love")], "context": "Part of the second commandment at Sinai.", "commentary": "His Word promises enduring love to the obedient."},
            {"verse": "Ex 20:11", "truth": "Sabbath set", "witnesses": [("Gen 2:3", "Day blessed"), ("Ex 31:17", "Sign forever")], "context": "God commands rest in the fourth commandment.", "commentary": "His Word sanctifies time for His glory."},
            {"verse": "Ex 23:25", "truth": "Free from disease", "witnesses": [("Deut 7:15", "No sickness"), ("Ps 91:10", "No plague near")], "context": "God’s promise to Israel in covenant obedience.", "commentary": "His Word guards life with His protection."},
            {"verse": "Ex 33:20", "truth": "Cannot see My face", "witnesses": [("John 1:18", "No one has seen"), ("1 Tim 6:16", "Unapproachable light")], "context": "God speaks to Moses on Sinai’s peak.", "commentary": "His Word reveals His holiness, beyond sight."},
            {"verse": "Lev 19:2", "truth": "Be holy", "witnesses": [("1 Pet 1:16", "Be holy as I am"), ("Lev 11:44", "Consecrate yourselves")], "context": "God commands holiness in Israel’s laws.", "commentary": "His Word calls us to reflect His nature."},
            {"verse": "Num 11:16", "truth": "Seventy elders chosen", "witnesses": [("Ex 24:1", "Elders called"), ("Num 11:25", "Spirit on them")], "context": "God aids Moses with Spirit-filled leaders.", "commentary": "His Word empowers service among His people."},
            {"verse": "Deut 5:26", "truth": "Living God", "witnesses": [("Josh 3:10", "Living God among"), ("Jer 10:10", "True living God")], "context": "Moses reiterates God’s law to Israel.", "commentary": "His Word proclaims His living presence."},
            {"verse": "Deut 6:4", "truth": "Lord is one", "witnesses": [("Mark 12:29", "One Lord"), ("Zech 14:9", "One name")], "context": "The Shema, Israel’s core confession.", "commentary": "His Word declares His singular sovereignty."},
            {"verse": "Deut 7:15", "truth": "No disease", "witnesses": [("Ex 15:26", "Heals all"), ("Ps 103:3", "Heals diseases")], "context": "God’s covenant blessings for obedience.", "commentary": "His Word secures health through faithfulness."},
            {"verse": "Deut 28:4", "truth": "Fruit of womb blessed", "witnesses": [("Gen 1:28", "Be fruitful"), ("Ps 127:3", "Children a reward")], "context": "Blessings promised for covenant keepers.", "commentary": "His Word multiplies life as a gift."},
            {"verse": "Deut 28:7", "truth": "Enemies defeated", "witnesses": [("Ex 23:22", "Enemies subdued"), ("Ps 18:39", "Girded for battle")], "context": "Victory promised in covenant obedience.", "commentary": "His Word ensures triumph over opposition."},
            {"verse": "Deut 28:8", "truth": "Blessing on barns", "witnesses": [("Deut 28:5", "Basket blessed"), ("Prov 3:10", "Barns filled")], "context": "Material blessings for Israel’s faithfulness.", "commentary": "His Word prospers those who trust Him."},
            {"verse": "Deut 28:9", "truth": "Holy to the Lord", "witnesses": [("Ex 19:6", "Holy nation"), ("1 Pet 2:9", "Holy priesthood")], "context": "God sets Israel apart in covenant.", "commentary": "His Word consecrates His people."},
            {"verse": "Deut 28:16-18", "truth": "Cursed ground", "witnesses": [("Gen 3:17", "Ground cursed"), ("Deut 28:23", "Sky like bronze")], "context": "Curses for covenant disobedience.", "commentary": "His Word warns of consequences, yet offers redemption."},
            {"verse": "Deut 28:22", "truth": "Wasting disease", "witnesses": [("Lev 26:16", "Fever consumes"), ("Deut 28:61", "Every plague")], "context": "Part of curses for breaking covenant.", "commentary": "His Word’s justice is sure when defied."},
            {"verse": "Deut 28:25", "truth": "Defeated by enemies", "witnesses": [("Lev 26:17", "Flee before foes"), ("Deut 28:7", "Reversed blessing")], "context": "Defeat promised for disobedience.", "commentary": "His Word reverses favor when rejected."},
            {"verse": "Deut 28:63", "truth": "Uprooted from land", "witnesses": [("Deut 29:28", "Cast out"), ("Jer 1:10", "Uproot nations")], "context": "Exile foretold for covenant breakers.", "commentary": "His Word enforces His holy will."},
            {"verse": "Deut 32:4", "truth": "Rock of justice", "witnesses": [("Ps 18:2", "My rock"), ("Isa 30:29", "Rock of Israel")], "context": "Moses’ song exalts God’s character.", "commentary": "His Word stands firm as righteousness."},
            {"verse": "Judg 6:24", "truth": "Jehovah Shalom peace", "witnesses": [("Num 6:26", "Peace given"), ("Isa 9:6", "Prince of Peace")], "context": "Gideon builds an altar after God’s call.", "commentary": "His Word brings peace amidst chaos."},
            {"verse": "1 Sam 1:3", "truth": "Jehovah Sabaoth hosts", "witnesses": [("Ps 24:10", "Lord of hosts"), ("Isa 6:3", "Hosts fill earth")], "context": "Hannah prays to the Lord of hosts.", "commentary": "His Word commands all heavenly armies."},
            {"verse": "Ps 10:16", "truth": "King rules forever", "witnesses": [("Ps 29:10", "Lord enthroned"), ("Dan 4:34", "Dominion eternal")], "context": "A psalm exalting God’s reign.", "commentary": "His Word’s kingship is everlasting."},
            {"verse": "Ps 19:1", "truth": "Heavens declare His glory", "witnesses": [("Ps 8:3", "Works of fingers"), ("Rom 1:20", "Creation reveals")], "context": "David praises God’s creation.", "commentary": "His Word speaks through the skies."},
            {"verse": "Ps 50:10", "truth": "Cattle on thousand hills", "witnesses": [("Ps 24:1", "Earth is His"), ("Hag 2:8", "Silver and gold")], "context": "God asserts ownership over all.", "commentary": "His Word claims all as His possession."},
            {"verse": "Ps 90:2", "truth": "God from everlasting", "witnesses": [("Ps 93:2", "Throne eternal"), ("1 Tim 1:17", "King eternal")], "context": "Moses prays to the eternal God.", "commentary": "His Word transcends time itself."},
            {"verse": "Ps 104:31", "truth": "Glory endures forever", "witnesses": [("Ps 102:12", "Renown endures"), ("Isa 6:3", "Glory fills earth")], "context": "A hymn to God’s creation.", "commentary": "His Word’s glory is unending."},
            {"verse": "Ps 111:3", "truth": "Righteousness forever", "witnesses": [("Ps 119:142", "Righteousness eternal"), ("Isa 51:6", "Righteousness stands")], "context": "Praise for God’s righteous works.", "commentary": "His Word upholds eternal justice."},
            {"verse": "Ps 118:16", "truth": "Right hand exalted", "witnesses": [("Ex 15:6", "Hand glorious"), ("Ps 98:1", "Right hand won")], "context": "A song of God’s deliverance.", "commentary": "His Word’s power prevails."},
            {"verse": "Ps 118:23", "truth": "Lord has done this", "witnesses": [("Ps 118:22", "Stone rejected"), ("Matt 21:42", "Cornerstone")], "context": "Celebration of God’s marvelous acts.", "commentary": "His Word builds salvation’s foundation."},
            {"verse": "Ps 119:89", "truth": "Word settled in heaven", "witnesses": [("Ps 119:152", "Founded forever"), ("Luke 21:33", "Words endure")], "context": "A meditation on God’s law.", "commentary": "His Word is eternally established."},
            {"verse": "Ps 135:13", "truth": "Name endures forever", "witnesses": [("Ps 102:12", "Renown endures"), ("Ex 3:15", "Name forever")], "context": "Praise for God’s enduring fame.", "commentary": "His Word’s name outlasts all."},
            {"verse": "Ps 136:1", "truth": "Love endures forever", "witnesses": [("1 Cor 13:8", "Love never fails"), ("Jer 31:3", "Everlasting love")], "context": "A refrain of God’s steadfast love.", "commentary": "His Word’s love is unbreakable."},
            {"verse": "Ps 145:13", "truth": "Kingdom everlasting", "witnesses": [("Dan 4:3", "Kingdom endures"), ("Ps 10:16", "King forever")], "context": "David extols God’s eternal reign.", "commentary": "His Word rules without end."},
            {"verse": "Isa 1:17", "truth": "Seek justice", "witnesses": [("Mic 6:8", "Do justice"), ("Ps 82:3", "Defend the weak")], "context": "Isaiah calls Judah to righteousness.", "commentary": "His Word demands justice for all."},
            {"verse": "Isa 3:15", "truth": "Contrite in heart", "witnesses": [("Ps 51:17", "Broken spirit"), ("Isa 66:2", "Humble heart")], "context": "God judges Judah’s pride.", "commentary": "His Word values humility."},
            {"verse": "Isa 6:3", "truth": "Holy One", "witnesses": [("Lev 19:2", "Be holy"), ("Rev 4:8", "Holy, holy, holy")], "context": "Isaiah’s vision of God’s throne.", "commentary": "His Word exalts His holiness."},
            {"verse": "Isa 9:6", "truth": "Prince of Peace", "witnesses": [("John 16:33", "Peace in Me"), ("Eph 2:14", "Our peace")], "context": "Prophecy of the Messiah’s birth.", "commentary": "His Word brings peace through Christ."},
            {"verse": "Isa 14:12-14", "truth": "Satan fell", "witnesses": [("Luke 10:18", "Satan fall"), ("Rev 12:9", "Cast down")], "context": "Judgment on Babylon’s king, linked to Satan.", "commentary": "His Word reveals evil’s defeat."},
            {"verse": "Isa 40:8", "truth": "Word stands forever", "witnesses": [("Matt 24:35", "Words never pass"), ("1 Pet 1:25", "Word endures")], "context": "Comfort to Israel in exile.", "commentary": "His Word’s permanence outlasts all."},
            {"verse": "Isa 43:7", "truth": "Created for My glory", "witnesses": [("Isa 48:11", "My glory"), ("Rom 11:36", "All for Him")], "context": "God’s promise to redeem Israel.", "commentary": "His Word purposes us for His praise."},
            {"verse": "Isa 49:7", "truth": "Holy One of Israel", "witnesses": [("Isa 12:6", "Holy One in midst"), ("Ps 71:22", "Holy One")], "context": "The Servant’s mission to the nations.", "commentary": "His Word sanctifies His chosen."},
            {"verse": "Isa 52:10", "truth": "Arm made bare", "witnesses": [("Ps 98:1", "Arm won victory"), ("Isa 53:1", "Arm revealed")], "context": "God’s salvation displayed to all.", "commentary": "His Word acts mightily for redemption."},
            {"verse": "Isa 53:2", "truth": "No form or majesty", "witnesses": [("Phil 2:7", "Form of servant"), ("Isa 52:14", "Marred appearance")], "context": "The Suffering Servant’s humble state.", "commentary": "His Word’s glory shines in humility."},
            {"verse": "Isa 53:5", "truth": "Healed by His stripes", "witnesses": [("1 Pet 2:24", "By wounds healed"), ("Matt 8:17", "Took infirmities")], "context": "The Servant bears our sins.", "commentary": "His Word heals through sacrifice."},
            {"verse": "Isa 53:7", "truth": "Lamb to slaughter", "witnesses": [("John 1:29", "Lamb of God"), ("1 Pet 1:19", "Lamb without blemish")], "context": "The Servant silently endures suffering.", "commentary": "His Word fulfills atonement’s plan."},
            {"verse": "Isa 55:11", "truth": "Word accomplishes His will", "witnesses": [("Heb 4:12", "Word is active"), ("Jer 23:29", "Word like fire")], "context": "God’s invitation to seek Him.", "commentary": "His Word never fails its purpose."},
            {"verse": "Isa 57:15", "truth": "Contrite in spirit", "witnesses": [("Ps 34:18", "Near the broken"), ("Isa 66:2", "Contrite heart")], "context": "God’s comfort to the humble.", "commentary": "His Word dwells with the lowly."},
            {"verse": "Isa 66:1", "truth": "Earth My footstool", "witnesses": [("Matt 5:35", "Earth His footstool"), ("Acts 7:49", "Heaven My throne")], "context": "God’s declaration of His greatness.", "commentary": "His Word reigns over all creation."},
            {"verse": "Jer 23:6", "truth": "Jehovah Tsidkenu righteousness", "witnesses": [("Jer 33:16", "Lord our righteousness"), ("Rom 3:22", "Righteousness of God")], "context": "Prophecy of a righteous Branch.", "commentary": "His Word is our righteousness."},
            {"verse": "Dan 2:44", "truth": "Kingdom stands eternal", "witnesses": [("Ps 145:13", "Kingdom everlasting"), ("Dan 7:14", "Dominion forever")], "context": "Daniel interprets Nebuchadnezzar’s dream.", "commentary": "His Word establishes an unshakable reign."},
            {"verse": "Dan 4:25", "truth": "Most High rules", "witnesses": [("Dan 4:34", "Dominion eternal"), ("Ps 103:19", "Throne in heavens")], "context": "Nebuchadnezzar humbled by God.", "commentary": "His Word governs all kings."},
            {"verse": "Dan 7:9", "truth": "Ancient of Days", "witnesses": [("Rev 1:14", "Hair white"), ("Ps 102:25", "Of old You laid")], "context": "Daniel’s vision of God’s throne.", "commentary": "His Word reveals His timeless majesty."},
            {"verse": "Amos 5:24", "truth": "Justice rolls down", "witnesses": [("Isa 1:17", "Seek justice"), ("Ps 89:14", "Justice foundation")], "context": "Amos condemns Israel’s injustice.", "commentary": "His Word demands righteousness flow."},
            {"verse": "Mic 6:8", "truth": "Do justice", "witnesses": [("Zech 7:9", "Administer justice"), ("Prov 21:3", "Justice pleasing")], "context": "Micah sums up God’s requirements.", "commentary": "His Word guides righteous living."},
            {"verse": "Mal 3:6", "truth": "God unchanging", "witnesses": [("Heb 13:8", "Same forever"), ("James 1:17", "No variation")], "context": "God’s promise amid judgment.", "commentary": "His Word’s constancy endures."},
            {"verse": "Hab 1:13", "truth": "Eyes too pure for evil", "witnesses": [("Ps 5:4", "No evil dwells"), ("Isa 6:5", "Holy presence")], "context": "Habakkuk questions God’s justice.", "commentary": "His Word’s purity judges all."},
            {"verse": "Matt 3:16", "truth": "Spirit as dove", "witnesses": [("Luke 3:22", "Dove descended"), ("John 1:32", "Spirit descending")], "context": "Jesus’ baptism by John.", "commentary": "His Word reveals the Spirit’s presence."},
            {"verse": "Matt 3:17", "truth": "This is my Son", "witnesses": [("Matt 17:5", "Beloved Son"), ("John 1:34", "Son of God")], "context": "God affirms Jesus at baptism.", "commentary": "His Word declares the Son’s identity."},
            {"verse": "Matt 5:3-12", "truth": "Blessed are the meek", "witnesses": [("Luke 6:20-23", "Blessed poor"), ("Ps 37:11", "Meek inherit")], "context": "Jesus’ Sermon on the Mount.", "commentary": "His Word blesses the humble."},
            {"verse": "Matt 5:17", "truth": "Fulfilled the Law", "witnesses": [("Rom 10:4", "End of law"), ("Gal 3:24", "Law led to Christ")], "context": "Jesus teaches on the Mount.", "commentary": "His Word completes God’s law."},
            {"verse": "Matt 5:37", "truth": "Yes be yes", "witnesses": [("James 5:12", "Let yes be yes"), ("Matt 5:34", "No oaths")], "context": "Jesus on truthfulness in speech.", "commentary": "His Word demands integrity."},
            {"verse": "Matt 6:6", "truth": "Father unseen", "witnesses": [("John 4:24", "God is spirit"), ("1 Tim 1:17", "Invisible God")], "context": "Jesus teaches private prayer.", "commentary": "His Word invites intimate communion."},
            {"verse": "Matt 10:28", "truth": "Fear Him who destroys", "witnesses": [("Luke 12:5", "Fear Him"), ("Heb 10:31", "Fearful judgment")], "context": "Jesus sends the disciples.", "commentary": "His Word commands reverent awe."},
            {"verse": "Matt 11:29", "truth": "Gentle and lowly", "witnesses": [("Phil 2:8", "Humbled Himself"), ("Zech 9:9", "Lowly on donkey")], "context": "Jesus offers rest to the weary.", "commentary": "His Word’s meekness draws us."},
            {"verse": "Matt 12:12", "truth": "Good on Sabbath", "witnesses": [("Mark 3:4", "Lawful to do good"), ("Luke 6:9", "Good on Sabbath")], "context": "Jesus heals on the Sabbath.", "commentary": "His Word prioritizes mercy."},
            {"verse": "Matt 12:24", "truth": "Called Him demon", "witnesses": [("John 8:48", "Said demon-possessed"), ("Mark 3:22", "By Beelzebul")], "context": "Pharisees accuse Jesus.", "commentary": "His Word faces rejection, yet prevails."},
            {"verse": "Matt 12:31-32", "truth": "Blasphemy unforgiven", "witnesses": [("Mark 3:29", "Eternal sin"), ("Luke 12:10", "Not forgiven")], "context": "Jesus warns against blaspheming the Spirit.", "commentary": "His Word sets eternal boundaries."},
            {"verse": "Matt 13:24-30", "truth": "Wheat and weeds", "witnesses": [("Matt 13:38", "Field is world"), ("Matt 13:40", "Burned at end")], "context": "Jesus’ parable of the kingdom.", "commentary": "His Word discerns good from evil."},
            {"verse": "Matt 13:30", "truth": "Harvest at end", "witnesses": [("Rev 14:15", "Harvest time"), ("Joel 3:13", "Harvest ripe")], "context": "Conclusion of the wheat and weeds parable.", "commentary": "His Word promises final judgment."},
            {"verse": "Matt 13:34-35", "truth": "Spoke in parables", "witnesses": [("Mark 4:34", "Only parables"), ("Ps 78:2", "Utter dark sayings")], "context": "Jesus teaches the crowds.", "commentary": "His Word unveils mysteries through stories."},
            {"verse": "Matt 18:3", "truth": "Like children", "witnesses": [("Mark 10:15", "As a child"), ("Luke 18:17", "Receive as child")], "context": "Jesus blesses little children.", "commentary": "His Word calls for simple faith."},
            {"verse": "Matt 19:19", "truth": "Honor parents", "witnesses": [("Ex 20:12", "Honor father"), ("Eph 6:2", "First command")], "context": "Jesus answers the rich young ruler.", "commentary": "His Word upholds familial duty."},
            {"verse": "Matt 22:37-40", "truth": "Love God and neighbor", "witnesses": [("Deut 6:5", "Love Lord"), ("Lev 19:18", "Love neighbor")], "context": "Jesus sums up the law.", "commentary": "His Word centers on love."},
            {"verse": "Matt 23:27", "truth": "Woe to hypocrites", "witnesses": [("Matt 23:13", "Woe to scribes"), ("Luke 11:44", "Unseen tombs")], "context": "Jesus denounces the Pharisees.", "commentary": "His Word exposes false piety."},
            {"verse": "Matt 24:35", "truth": "Words never pass away", "witnesses": [("Luke 21:33", "Words endure"), ("Mark 13:31", "Will not pass")], "context": "Jesus foretells the end times.", "commentary": "His Word’s endurance is eternal."},
            {"verse": "Matt 25:31", "truth": "Son of Man judges", "witnesses": [("John 5:27", "Authority to judge"), ("Matt 16:27", "Repay each")], "context": "Parable of the sheep and goats.", "commentary": "His Word decrees final justice."},
            {"verse": "Matt 27:50", "truth": "Jesus died", "witnesses": [("John 19:30", "Gave up spirit"), ("Mark 15:37", "Breathed last")], "context": "Crucifixion at Golgotha.", "commentary": "His Word fulfills redemption’s cost."},
            {"verse": "Matt 28:6", "truth": "He is risen", "witnesses": [("Luke 24:6", "Not here"), ("Mark 16:6", "He has risen")], "context": "Angel announces resurrection.", "commentary": "His Word conquers death."},
            {"verse": "Matt 28:18", "truth": "All authority given", "witnesses": [("Dan 7:14", "Dominion given"), ("John 17:2", "Authority over all")], "context": "Great Commission before ascension.", "commentary": "His Word reigns supreme."},
            {"verse": "Matt 28:19-20", "truth": "Make disciples", "witnesses": [("Mark 16:15", "Preach gospel"), ("Acts 1:8", "Witness to ends")], "context": "Jesus’ final command to the Eleven.", "commentary": "His Word spreads His kingdom."},
            {"verse": "Mark 2:27", "truth": "Sabbath for man", "witnesses": [("Ex 20:10", "Day of rest"), ("Matt 12:8", "Lord of Sabbath")], "context": "Jesus defends His disciples.", "commentary": "His Word prioritizes human need."},
            {"verse": "Mark 14:36", "truth": "Abba Father", "witnesses": [("Rom 8:15", "Cry Abba"), ("Gal 4:6", "Abba Father")], "context": "Jesus prays in Gethsemane.", "commentary": "His Word reveals intimate sonship."},
            {"verse": "Mark 16:19", "truth": "Ascended to right hand", "witnesses": [("Acts 1:9", "Taken up"), ("Heb 1:3", "Sat at right hand")], "context": "Jesus ascends after resurrection.", "commentary": "His Word exalts Him to glory."},
            {"verse": "Luke 1:35", "truth": "Born of Spirit", "witnesses": [("Matt 1:20", "Conceived by Spirit"), ("Luke 1:31", "Son of God")], "context": "Angel announces Jesus’ birth.", "commentary": "His Word incarnates through the Spirit."},
            {"verse": "Luke 3:23", "truth": "Jesus at thirty", "witnesses": [("Luke 3:21", "Baptized"), ("John 2:20", "Temple age context")], "context": "Jesus begins His ministry.", "commentary": "His Word marks His appointed time."},
            {"verse": "Luke 3:23-38", "truth": "25 generations", "witnesses": [("Matt 1:17", "Genealogy spans"), ("Gen 5:3", "Adam to Seth")], "context": "Luke traces Jesus’ lineage.", "commentary": "His Word connects all history."},
            {"verse": "Luke 4:18", "truth": "Spirit of the Lord", "witnesses": [("Isa 61:1", "Anointed me"), ("Acts 10:38", "Anointed with Spirit")], "context": "Jesus reads Isaiah in Nazareth.", "commentary": "His Word fulfills prophetic anointing."},
            {"verse": "John 1:1", "truth": "Word was God", "witnesses": [("Gen 1:1", "God created"), ("Col 1:16", "All created by Him")], "context": "John’s prologue on the Logos.", "commentary": "His Word is divine and eternal."},
            {"verse": "John 1:5", "truth": "Light shines in darkness", "witnesses": [("1 John 2:8", "Darkness passing"), ("John 12:46", "Light in world")], "context": "John describes Christ’s coming.", "commentary": "His Word overcomes all darkness."},
            {"verse": "John 1:10", "truth": "World did not know Him", "witnesses": [("John 16:3", "Did not know"), ("1 Cor 2:8", "None understood")], "context": "John laments the world’s rejection.", "commentary": "His Word reveals despite blindness."},
            {"verse": "John 1:12", "truth": "Children of God", "witnesses": [("Rom 8:16", "Sons of God"), ("Gal 3:26", "Children by faith")], "context": "John offers adoption through belief.", "commentary": "His Word grants divine sonship."},
            {"verse": "John 1:16", "truth": "Grace upon grace", "witnesses": [("Eph 2:8", "Saved by grace"), ("Rom 5:17", "Abundance of grace")], "context": "John celebrates Christ’s fullness.", "commentary": "His Word overflows with mercy."},
            {"verse": "John 1:29", "truth": "Lamb of God", "witnesses": [("Isa 53:7", "Led to slaughter"), ("Rev 5:6", "Lamb standing")], "context": "John the Baptist hails Jesus.", "commentary": "His Word atones as the Lamb."},
            {"verse": "John 3:5", "truth": "Born of water and Spirit", "witnesses": [("Titus 3:5", "Renewal by Spirit"), ("John 7:38", "Living water")], "context": "Jesus teaches Nicodemus.", "commentary": "His Word regenerates through the Spirit."},
            {"verse": "John 3:8", "truth": "Spirit unseen", "witnesses": [("John 20:29", "Blessed unseen"), ("Acts 2:2", "Wind sound")], "context": "Jesus explains rebirth to Nicodemus.", "commentary": "His Word moves mysteriously."},
            {"verse": "John 3:16", "truth": "God gave His Son", "witnesses": [("Rom 5:8", "Love in Christ"), ("1 John 4:9", "Son sent")], "context": "Jesus reveals God’s plan to Nicodemus.", "commentary": "His Word’s love redeems eternally."},
            {"verse": "John 3:17", "truth": "To save the world", "witnesses": [("John 12:47", "Not to judge"), ("1 Tim 2:4", "All saved")], "context": "Jesus’ mission clarified to Nicodemus.", "commentary": "His Word seeks salvation for all."},
            {"verse": "John 4:24", "truth": "God is spirit", "witnesses": [("John 1:18", "No one has seen"), ("1 Tim 1:17", "Invisible God")], "context": "Jesus speaks to the Samaritan woman.", "commentary": "His Word defines His spiritual nature."},
            {"verse": "John 5:24", "truth": "Eternal life given", "witnesses": [("John 3:36", "Life in Son"), ("1 John 5:11", "Life eternal")], "context": "Jesus teaches on judgment and life.", "commentary": "His Word grants everlasting life."},
            {"verse": "John 6:35", "truth": "Bread of life", "witnesses": [("John 6:48", "I am bread"), ("Matt 4:4", "Live by Word")], "context": "Jesus feeds the five thousand.", "commentary": "His Word sustains spiritually."},
            {"verse": "John 8:12", "truth": "Light of the world", "witnesses": [("John 1:4", "Life was light"), ("1 John 1:5", "God is light")], "context": "Jesus speaks in the temple.", "commentary": "His Word illuminates all paths."},
            {"verse": "John 10:11", "truth": "Good Shepherd", "witnesses": [("Ps 23:1", "Lord my shepherd"), ("Heb 13:20", "Great Shepherd")], "context": "Jesus contrasts with false shepherds.", "commentary": "His Word guides and protects."},
            {"verse": "John 11:25", "truth": "Resurrection and life", "witnesses": [("John 5:21", "Raises the dead"), ("1 Cor 15:22", "Alive in Christ")], "context": "Jesus comforts Martha before raising Lazarus.", "commentary": "His Word defeats death."},
            {"verse": "John 14:6", "truth": "Way, truth, life", "witnesses": [("John 1:17", "Truth through Jesus"), ("Acts 4:12", "No other name")], "context": "Jesus comforts His disciples.", "commentary": "His Word is the only path."},
            {"verse": "John 15:1", "truth": "True vine", "witnesses": [("Isa 5:7", "Vineyard of Lord"), ("John 15:5", "Branches in Me")], "context": "Jesus teaches on abiding.", "commentary": "His Word connects us to life."},
            {"verse": "John 16:33", "truth": "Peace in Me", "witnesses": [("Phil 4:7", "Peace of God"), ("Col 3:15", "Peace rule hearts")], "context": "Jesus prepares disciples for His departure.", "commentary": "His Word overcomes the world."},
            {"verse": "John 17:3", "truth": "Eternal life knowing God", "witnesses": [("1 John 5:20", "True God"), ("John 10:28", "Life eternal")], "context": "Jesus prays for His followers.", "commentary": "His Word reveals true knowledge."},
            {"verse": "John 20:31", "truth": "Believe and have life", "witnesses": [("John 3:15", "Believe for life"), ("Acts 16:31", "Believe and saved")], "context": "John states his Gospel’s purpose.", "commentary": "His Word offers life through faith."},
            {"verse": "Acts 1:8", "truth": "Witness to ends", "witnesses": [("Matt 28:19", "Make disciples"), ("Mark 16:15", "Preach gospel")], "context": "Jesus’ last words before ascension.", "commentary": "His Word empowers global mission."},
            {"verse": "Acts 2:4", "truth": "Filled with Spirit", "witnesses": [("Acts 1:5", "Baptized with Spirit"), ("Eph 5:18", "Be filled")], "context": "Pentecost brings the Spirit.", "commentary": "His Word fulfills the promise."},
            {"verse": "Acts 4:12", "truth": "Salvation in no other", "witnesses": [("John 14:6", "Only way"), ("1 Tim 2:5", "One mediator")], "context": "Peter preaches to the Sanhedrin.", "commentary": "His Word is the sole savior."},
            {"verse": "Rom 1:16", "truth": "Gospel is power", "witnesses": [("1 Cor 1:18", "Power to save"), ("Mark 16:15", "Preach gospel")], "context": "Paul introduces his letter to Rome.", "commentary": "His Word saves through faith."},
            {"verse": "Rom 3:23", "truth": "All have sinned", "witnesses": [("Gen 3:6", "Sin entered"), ("Rom 5:12", "Death through sin")], "context": "Paul explains universal need for grace.", "commentary": "His Word reveals our need."},
            {"verse": "Rom 5:8", "truth": "Love in Christ", "witnesses": [("John 3:16", "God gave Son"), ("1 John 4:10", "Sent His Son")], "context": "Paul on God’s love for sinners.", "commentary": "His Word demonstrates love."},
            {"verse": "Rom 6:23", "truth": "Gift of eternal life", "witnesses": [("John 10:28", "Life eternal"), ("Eph 2:8", "Gift of God")], "context": "Paul contrasts sin’s wages with grace.", "commentary": "His Word offers life freely."},
            {"verse": "Rom 8:1", "truth": "No condemnation", "witnesses": [("John 3:18", "Not condemned"), ("Rom 5:1", "Peace with God")], "context": "Paul comforts believers in Christ.", "commentary": "His Word frees from judgment."},
            {"verse": "Rom 8:28", "truth": "All things work for good", "witnesses": [("Gen 50:20", "Meant for good"), ("Phil 1:6", "Good work")], "context": "Paul assures believers of God’s plan.", "commentary": "His Word promises providence."},
            {"verse": "1 Cor 1:18", "truth": "Cross is power", "witnesses": [("Gal 6:14", "Boast in cross"), ("Rom 1:16", "Gospel power")], "context": "Paul defends the cross to Corinth.", "commentary": "His Word saves through the cross."},
            {"verse": "1 Cor 13:13", "truth": "Faith, hope, love", "witnesses": [("Heb 11:1", "Faith is"), ("Col 1:5", "Hope in heaven")], "context": "Paul exalts love above all.", "commentary": "His Word endures in love."},
            {"verse": "1 Cor 15:22", "truth": "Alive in Christ", "witnesses": [("Rom 6:11", "Alive to God"), ("John 11:25", "Resurrection life")], "context": "Paul on resurrection hope.", "commentary": "His Word restores life."},
            {"verse": "2 Cor 5:17", "truth": "New creation", "witnesses": [("Gal 6:15", "New creation"), ("Isa 65:17", "New heavens")], "context": "Paul on reconciliation in Christ.", "commentary": "His Word renews all things."},
            {"verse": "Gal 2:20", "truth": "Christ lives in me", "witnesses": [("Col 1:27", "Christ in you"), ("John 14:20", "I in them")], "context": "Paul on faith’s power.", "commentary": "His Word indwells believers."},
            {"verse": "Eph 2:8-9", "truth": "Saved by grace", "witnesses": [("Rom 3:24", "Grace justified"), ("Titus 3:7", "Grace heirs")], "context": "Paul on salvation’s source.", "commentary": "His Word gifts salvation."},
            {"verse": "Phil 2:9-11", "truth": "Name above all", "witnesses": [("Acts 4:12", "No other name"), ("Rev 19:16", "King of kings")], "context": "Paul exalts Christ’s humility and glory.", "commentary": "His Word exalts Jesus."},
            {"verse": "Col 1:16", "truth": "All created by Him", "witnesses": [("John 1:3", "All through Him"), ("Heb 1:2", "Made worlds")], "context": "Paul on Christ’s supremacy.", "commentary": "His Word creates everything."},
            {"verse": "1 Thess 4:17", "truth": "Caught up together", "witnesses": [("1 Cor 15:52", "Changed in twinkling"), ("John 14:3", "Take to Myself")], "context": "Paul comforts on Christ’s return.", "commentary": "His Word promises reunion."},
            {"verse": "Heb 1:3", "truth": "Upholds all by Word", "witnesses": [("Col 1:17", "All holds together"), ("Ps 33:6", "Word made heavens")], "context": "Hebrews exalts Christ’s deity.", "commentary": "His Word sustains creation."},
            {"verse": "Heb 4:12", "truth": "Word pierces soul", "witnesses": [("Jer 23:29", "Like fire"), ("Eph 6:17", "Sword of Spirit")], "context": "Hebrews on God’s living Word.", "commentary": "His Word discerns all."},
            {"verse": "Heb 11:1", "truth": "Faith is assurance", "witnesses": [("Rom 4:20", "Strong in faith"), ("2 Cor 5:7", "Walk by faith")], "context": "Hebrews defines faith.", "commentary": "His Word anchors belief."},
            {"verse": "James 1:17", "truth": "Every good gift", "witnesses": [("Ps 84:11", "Good things"), ("Rom 8:32", "Gave His Son")], "context": "James on God’s unchanging goodness.", "commentary": "His Word blesses perfectly."},
            {"verse": "1 Pet 1:25", "truth": "Word endures forever", "witnesses": [("Isa 40:8", "Stands forever"), ("Matt 24:35", "Never pass")], "context": "Peter quotes Isaiah on the Word.", "commentary": "His Word remains eternal."},
            {"verse": "1 John 1:1", "truth": "Word of life", "witnesses": [("John 1:1", "Word was God"), ("Phil 2:16", "Word of life")], "context": "John testifies to Christ.", "commentary": "His Word embodies life."},
            {"verse": "1 John 4:8", "truth": "God is love", "witnesses": [("John 3:16", "God gave Son"), ("Rom 5:8", "Love in Christ")], "context": "John defines God’s nature.", "commentary": "His Word reveals love’s essence."},
            {"verse": "Rev 1:8", "truth": "Alpha and Omega", "witnesses": [("Rev 22:13", "First and Last"), ("Isa 44:6", "First and Last")], "context": "Christ speaks to John.", "commentary": "His Word spans eternity."},
            {"verse": "Rev 19:16", "truth": "King of kings", "witnesses": [("1 Tim 6:15", "King of kings"), ("Dan 2:47", "God of kings")], "context": "Christ returns in glory.", "commentary": "His Word reigns over all."},
            {"verse": "Rev 21:1", "truth": "New heaven and earth", "witnesses": [("Isa 65:17", "New heavens"), ("2 Pet 3:13", "New earth")], "context": "John sees the new creation.", "commentary": "His Word renews everything."},
            {"verse": "Rev 22:13", "truth": "First and Last", "witnesses": [("Rev 1:8", "Alpha and Omega"), ("Isa 48:12", "I am He")], "context": "Christ affirms His eternity.", "commentary": "His Word completes all."},
            {"verse": "Rev 22:20", "truth": "Come, Lord Jesus", "witnesses": [("Rev 22:17", "Come quickly"), ("1 Cor 16:22", "Maranatha")], "context": "The closing prayer of Revelation, longing for Christ’s return.", "commentary": "Affirms the eternal promise of His Word—Jesus will return as King."}
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
