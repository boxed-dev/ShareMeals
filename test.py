initial = '''Dynamo
Vanguard
hash7
OK
Code4Good
Kaccha Badaam
Web Warriors
Terra Wrist
TightSalt
Bug Slayers
TheBinaryBards
Gladiators
Tweepyzz
TechTitans
360in3D
RainCoatFam
TheIlluminati
Team Encoders
The Hackerati
Tech Titans
HardCoders
65something
XARCO
The Morris Worm
Jet Lagged Chef
Brew Codes
CMD CTRL
UNLOCKERS
Legion 501
Byte Me
Code Chaos
Code Nostalgia
MOPSY
TBD
greg.gg
Team Ninja
Dexter's Laboratory Lab Rats
BytebyByte
teamcats
The Utopians
D20
Codoholics
DARKdevs
CooCooBrains
Code_Hunters
Ctrl-Alt-Elite
Team Doritos
Midori's Den
Code Crew
Hayabooza
Werewolves
gilehri
happiHappiHappi
Trojan Horses
Bit Busters
Thrift
NoteTag
No Name
Insignia
Holden Madick
Silicon Sorcerers
MetaMinds
Null Set
Bhagwaan Bharose
Hidden Coders
Code Gladiators
Algorithm Assassins
somethingFosho
Bug Squashers
Destroyurr
coderunners
Blacklisted
Magnum
Real
PATHOS
Devgeeks
BYTEBUSTERS
Compiler Crew
MeteorMavericks
Glitch
Bakar Point
Bytes
Error404
Undercooked
Pokemon
Sharktooth
CHATGPT>>BARD
RoyalScots
Orcus
SKYNET
CW
Code Crusaders
arc
Code Synergy
SyntaxSorcerers
S4 Bucket
Alt+F4
TubeLite
TRYKATHONS
Cipher404
MemeDreamTeam
NYANNERS
Irregulars
Meretrix
Hack House
WeCare
CODENINJA
brocode
SHARKS
Gantt chart
404found
Circuit Surfers
Romeos
Aero
CODE_BREWERS.
NandankeBharose'''

inti_parti = initial.split('\n')

final = '''360in3D
Aero
Algorithm Assassins
Alt+F4
arc
Bakar Point
Bhagwaan Bharose
Blacklisted
Brew Codes
Bug Squashers
BYTEBUSTERS
BytebyByte
Bytes
CHATGPT>>BARD
Cipher404
Circuit Surfers
CMD CTRL
Code Chaos
Code Crew
Code Crusaders
Code Nostalgia
Code Synergy
CODE_BREWERS.
Code_Hunters
Code4Good
CODENINJA
coderunners
Codoholics
Compiler Crew
CooCooBrains
Ctrl-Alt-Elite
CW
D20
DARKdevs
Destroyurr
Devgeeks
Dexter's Laboratory Lab Rats
Dynamo
Error404
Gantt chart
gilehri
Gladiators
Glitch
greg.gg
Hack House
happiHappiHappi
HardCoders
hash7
Hidden Coders
Holden Madick
Insignia
Irregulars
Jet Lagged Chef
Legion 501
Magnum
MemeDreamTeam
Meretrix
MetaMinds
MeteorMavericks
Midori's Den
MOPSY
NandankeBharose
No Name
NoteTag
Null Set
NYANNERS
Orcus
PATHOS
Pokemon
Real
RoyalScots
S4 Bucket
SHARKS
Sharktooth
Silicon Sorcerers
SKYNET
somethingFosho
SyntaxSorcerers
TBD
Team Doritos
Team Encoders
Team Ninja
teamcats
Tech Titans
TechTitans
Terra Wrist
The Hackerati
The Morris Worm
The Utopians
TheBinaryBards
TheIlluminati
TightSalt
Trojan Horses
TRYKATHONS
TubeLite
Undercooked
UNLOCKERS
Vanguard
Web Warriors
WeCare
XARCO
Bitmines
Cascade
Closure'''

fini_parti = final.split('\n')

for i in inti_parti:
    if i not in fini_parti:
        print(f"{i} is disqualified")

