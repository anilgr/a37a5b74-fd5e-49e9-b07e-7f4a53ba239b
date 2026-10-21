import json

MAPPINGS = {
    # Day 361
    "MOVE TO ACTION": ("MOVE TO ACTION {ಕಾರ್ಯೋನ್ಮುಖನಾಗು/ಪ್ರೇರೇಪಿಸು}", {
        "DRIVE": "DRIVE {ಉತ್ತೇಜಿಸು}",
        "PROMPT": "PROMPT {ಪ್ರಚೋದಿಸು}",
        "PROPEL": "PROPEL {ಮುಂದೂಡು}",
        "PUSH": "PUSH {ಒತ್ತಡ ಹೇರು}",
    }),
    "UNO CARDS": ("UNO CARDS {ಊನೋ ಕಾರ್ಡ್‌ಗಳು}", {
        "DRAW": "DRAW {ಕಾರ್ಡ್ ಎತ್ತು}",
        "REVERSE": "REVERSE {ರಿವರ್ಸ್}",
        "SKIP": "SKIP {ಸ್ಕಿಪ್}",
        "WILD": "WILD {ವೈಲ್ಡ್}",
    }),
    "HAIL SIZE COMPARISONS": ("HAIL SIZE COMPARISONS {ಆಲಿಕಲ್ಲಿನ ಗಾತ್ರದ ಹೋಲಿಕೆಗಳು}", {
        "BASEBALL": "BASEBALL {ಬೇಸ್‌ಬಾಲ್ ಗಾತ್ರ}",
        "GRAPEFRUIT": "GRAPEFRUIT {ಮೋಸಂಬಿ ಗಾತ್ರ}",
        "MARBLE": "MARBLE {ಗೋಲಿ ಗಾತ್ರ}",
        "PEA": "PEA {ಬಟಾಣಿ ಗಾತ್ರ}",
    }),
    "PLACES WITH BENCHES": ("PLACES WITH BENCHES {ಬೆಂಚ್‌ಗಳಿರುವ ಸ್ಥಳಗಳು}", {
        "COURTROOM": "COURTROOM {ನ್ಯಾಯಾಲಯ}",
        "DUGOUT": "DUGOUT {ಡಗ್ಔಟ್}",
        "GYM": "GYM {ಜಿಮ್}",
        "PARK": "PARK {ಉದ್ಯಾನವನ}",
    }),

    # Day 362
    "DREAM UP": ("DREAM UP {ಕಲ್ಪಿಸಿಕೊ/ಯೋಚಿಸು}", {
        "CONCEIVE": "CONCEIVE {ಭಾವಿಸು}",
        "ENVISION": "ENVISION {ಮನಸ್ಸಿನಲ್ಲಿ ಕಾಣು}",
        "IMAGINE": "IMAGINE {ಕಲ್ಪಿಸಿಕೊ}",
        "PICTURE": "PICTURE {ಚಿತ್ರಿಸಿಕೊ}",
    }),
    "THIN COVERING": ("THIN COVERING {ತೆಳುವಾದ ಪದರ/ಹೊದಿಕೆ}", {
        "COAT": "COAT {ಲೇಪನ}",
        "FILM": "FILM {ತೆಳುಪದರ}",
        "LAYER": "LAYER {ಪದರ}",
        "SKIN": "SKIN {ಚರ್ಮ/ಹೊದಿಕೆ}",
    }),
    "REMOVE, AS CRUMBS": ("REMOVE, AS CRUMBS {ಹಿಟ್ಟಿನ ಪುಡಿ/ಕಸವನ್ನು ಒರೆಸಿ ತೆಗೆಯುವುದು}", {
        "BRUSH": "BRUSH {ಬ್ರಷ್ ಮಾಡು}",
        "FLICK": "FLICK {ತಟ್ಟು}",
        "SWEEP": "SWEEP {ಗುಡಿಸು}",
        "WIPE": "WIPE {ಒರೆಸು}",
    }),
    "VERBS FOR A SOFTWARE ENGINEER": ("VERBS FOR A SOFTWARE ENGINEER {ಸಾಫ್ಟ್‌ವೇರ್ ಎಂಜಿನಿಯರ್ ಮಾಡುವ ಕೆಲಸಗಳು}", {
        "CODE": "CODE {ಕೋಡಿಂಗ್}",
        "DEVELOP": "DEVELOP {ಡೆವಲಪ್}",
        "HACK": "HACK {ಹ್ಯಾಕ್}",
        "PROGRAM": "PROGRAM {ಪ್ರೋಗ್ರಾಮಿಂಗ್}",
    }),

    # Day 363
    "GRAB ONE\u2019S ATTENTION": ("GRAB ONE\u2019S ATTENTION {ಗಮನ ಸೆಳೆಯುವುದು}", {
        "ABSORB": "ABSORB {ತಲ್ಲೀನಗೊಳಿಸು}",
        "ENGROSS": "ENGROSS {ಆಕರ್ಷಿಸು}",
        "HOLD": "HOLD {ಹಿಡಿದಿಟ್ಟುಕೊ}",
        "RIVET": "RIVET {ಸೆರೆಹಿಡಿ}",
    }),
    "DOCUMENT WITH VIDEO": ("DOCUMENT WITH VIDEO {ವಿಡಿಯೋ ಚಿತ್ರೀಕರಣ}", {
        "FILM": "FILM {ಚಿತ್ರೀಕರಿಸು}",
        "RECORD": "RECORD {ದಾಖಲಿಸು}",
        "SHOOT": "SHOOT {ಶೂಟ್ ಮಾಡು}",
        "TAPE": "TAPE {ರೆಕಾರ್ಡ್ ಮಾಡು}",
    }),
    # Skip: ANAGRAMS (Pastel, Petals, Pleats, Staple)
    # Skip: PRETTY ___ (English collocations Good, Penny, Please, Woman)

    # Day 364
    "FEELING SOME TYPE OF WAY": ("FEELING SOME TYPE OF WAY {ಬೇಸರ/ಕೋಪದ ಭಾವನೆ}", {
        "BITTER": "BITTER {ಕಹಿ ಭಾವ}",
        "SALTY": "SALTY {ಕಿರಿಕಿರಿಗೊಂಡ}",
        "SORE": "SORE {ನೊಂದ}",
        "UPSET": "UPSET {ಅಸಮಾಧಾನ}",
    }),
    "THROW HERE AND THERE": ("THROW HERE AND THERE {ಚಲ್ಲಾಪಿಲ್ಲಿಯಾಗಿ ಹರಡುವುದು}", {
        "PEPPER": "PEPPER {ಸಿಂಪಡಿಸು}",
        "SCATTER": "SCATTER {ಚದುರಿಸು}",
        "SPRINKLE": "SPRINKLE {ಚುಮುಕಿಸು}",
        "STREW": "STREW {ಹರಡು}",
    }),
    "THINGS WITH LAYERS": ("THINGS WITH LAYERS {ಪದರಗಳನ್ನು ಹೊಂದಿರುವ ವಸ್ತುಗಳು}", {
        "CAKE": "CAKE {ಕೇಕ್}",
        "EARTH": "EARTH {ಭೂಮಿ}",
        "ONION": "ONION {ಈರುಳ್ಳಿ}",
        "PLYWOOD": "PLYWOOD {ಪ್ಲೈವುಡ್}",
    }),
    # Skip: ___ POTATO (English collocations Baked, Couch, Hot, Sweet)

    # Day 365
    "CORE": ("CORE {ತಿರುಳು/ಮೂಲಾಂಶ}", {
        "CRUX": "CRUX {ಮುಖ್ಯ ವಿಷಯ}",
        "ESSENCE": "ESSENCE {ಸತ್ವ}",
        "HEART": "HEART {ಹೃದಯ/ಕೇಂದ್ರ}",
        "SUBSTANCE": "SUBSTANCE {ತಿರುಳು}",
    }),
    "COMPLICATED": ("COMPLICATED {ಸಂಕೀರ್ಣ/ಕ್ಲಿಷ್ಟಕರ}", {
        "BAROQUE": "BAROQUE {ಅತಿಯಾದ ವಿವರವುಳ್ಳ}",
        "COMPLEX": "COMPLEX {ಸಂಕೀರ್ಣ}",
        "ELABORATE": "ELABORATE {ವಿಸ್ತೃತ}",
        "INVOLVED": "INVOLVED {ಗೋಜಲಾದ}",
    }),
    "SYMBOLS USED IN MAKING LISTS": ("SYMBOLS USED IN MAKING LISTS {ಪಟ್ಟಿ ತಯಾರಿಸಲು ಬಳಸುವ ಚಿಹ್ನೆಗಳು}", {
        "ARROW": "ARROW {ಬಾಣದ ಗುರುತು}",
        "BULLET": "BULLET {ಬುಲೆಟ್ ಪಾಯಿಂಟ್}",
        "CHECKBOX": "CHECKBOX {ಚೆಕ್‌ಬಾಕ್ಸ್}",
        "HYPHEN": "HYPHEN {ಹೈಫನ್/ಗೆರೆ}",
    }),
    # Skip: WHAT "CROSS" MIGHT MEAN (English polysemy Angry, Betray, Crucifix, Hybrid)

    # Day 366
    # Skip: HOMOPHONES (Bi, Buy, By, Bye)
    "MUSCLES, INFORMALLY": ("MUSCLES, INFORMALLY {ದೇಹದ ಸ್ನಾಯುಗಳ ಸಂಕ್ಷಿಪ್ತ ಹೆಸರುಗಳು}", {
        "AB": "AB {ಆಬ್ಸ್}",
        "PEC": "PEC {ಪೆಕ್ಸ್}",
        "QUAD": "QUAD {ಕ್ವಾಡ್ಸ್}",
        "TRI": "TRI {ಟ್ರೈಸೆಪ್ಸ್}",
    }),
    "MUSIC GENRES": ("MUSIC GENRES {ಸಂಗೀತ ಶೈಲಿಗಳು}", {
        "DUB": "DUB {ಡಬ್}",
        "EMO": "EMO {ಎಮೋ}",
        "POP": "POP {ಪಾಪ್}",
        "TRAP": "TRAP {ಟ್ರ್ಯಾಪ್}",
    }),
    "SETTINGS ON AN APPLIANCE KNOB": ("SETTINGS ON AN APPLIANCE KNOB {ವಿದ್ಯುತ್ ಉಪಕರಣಗಳ ನಿಯಂತ್ರಣ ಬಟನ್}", {
        "HI": "HI {ಹೈ}",
        "LO": "LO {ಲೋ}",
        "MED": "MED {ಮೀಡಿಯಂ}",
        "OFF": "OFF {ಆಫ್}",
    }),

    # Day 367
    "PLACES IN NEW YORK CITY": ("PLACES IN NEW YORK CITY {ನ್ಯೂಯಾರ್ಕ್ ನಗರದ ಪ್ರಸಿದ್ಧ ಪ್ರದೇಶಗಳು}", {
        "CHINATOWN": "CHINATOWN {ಚೈನಾಟೌನ್}",
        "DUMBO": "DUMBO {ಡಂಬೋ}",
        "MANHATTAN": "MANHATTAN {ಮ್ಯಾನ್‌ಹ್ಯಾಟನ್}",
        "WALL STREET": "WALL STREET {ವಾಲ್ ಸ್ಟ್ರೀಟ್}",
    }),
    # Skip: RHYMING TITLES (Be Kind Rewind, E.T., Fright Night, Kill Bill - English rhyme puns)
    # Skip: ENDING IN UNITS OF MEASUREMENT (Hedwig and the Angry Inch, My Left Foot, The Green Mile, The Longest Yard)
    # Skip: STARTING WITH ANIMALS (Beetlejuice, Foxy Brown, Dogma, Octopussy)

    # Day 368
    "ENJOY": ("ENJOY {ಮೆಚ್ಚು/ಇಷ್ಟಪಡು}", {
        "APPRECIATE": "APPRECIATE {ಪ್ರಶಂಸಿಸು}",
        "DIG": "DIG {ಇಷ್ಟಪಡು}",
        "FANCY": "FANCY {ಮೆಚ್ಚು}",
        "LIKE": "LIKE {ಇಷ್ಟವಾಗು}",
    }),
    "BLOCKBUSTER": ("BLOCKBUSTER {ಭರ್ಜರಿ ಯಶಸ್ಸು}", {
        "HIT": "HIT {ಹಿಟ್}",
        "SENSATION": "SENSATION {ಸಂಚಲನ}",
        "SMASH": "SMASH {ಸೂಪರ್ ಹಿಟ್}",
        "SUCCESS": "SUCCESS {ಯಶಸ್ಸು}",
    }),
    "CAMPAIGN SWAG": ("CAMPAIGN SWAG {ಚುನಾವಣಾ ಪ್ರಚಾರ ಸಾಮಗ್ರಿಗಳು}", {
        "BUTTON": "BUTTON {ಬ್ಯಾಡ್ಜ್}",
        "HAT": "HAT {ಟೋಪಿ}",
        "SHIRT": "SHIRT {ಟಿ-ಶರ್ಟ್}",
        "STICKER": "STICKER {ಸ್ಟಿಕ್ಕರ್}",
    }),
    # Skip: WORDS AFTER "COPY" (English collocations Cat, Editor, Paste, That)

    # Day 369
    "WRITING ASSIGNMENTS": ("WRITING ASSIGNMENTS {ಬರವಣಿಗೆಯ ಕಾರ್ಯಭಾರಗಳು}", {
        "ARTICLE": "ARTICLE {ಲೇಖನ}",
        "ESSAY": "ESSAY {ಪ್ರಬಂಧ}",
        "PAPER": "PAPER {ಸಂಶೋಧನಾ ಪ್ರಬಂಧ}",
        "REPORT": "REPORT {ವರದಿ}",
    }),
    "THINGS THAT ARE PINK": ("THINGS THAT ARE PINK {ಗುಲಾಬಿ ಬಣ್ಣದ ವಸ್ತುಗಳು}", {
        "BUBBLE GUM": "BUBBLE GUM {ಬಬಲ್‌ಗಮ್}",
        "CARNATION": "CARNATION {ಕಾರ್ನೇಷನ್ ಹೂ}",
        "ERASER": "ERASER {ರಬ್ಬರ್/ಎರೇಸರ್}",
        "FLAMINGO": "FLAMINGO {ಫ್ಲೆಮಿಂಗೋ ಹಕ್ಕಿ}",
    }),
    "NATO PHONETIC ALPHABET": ("NATO PHONETIC ALPHABET {ನ್ಯಾಟೋ ಫೋನೆಟಿಕ್ ಅಕ್ಷರಗಳು}", {
        "FOXTROT": "FOXTROT {ಫಾಕ್ಸ್‌ಟ್ರಾಟ್}",
        "HOTEL": "HOTEL {ಹೋಟೆಲ್}",
        "VICTOR": "VICTOR {ವಿಕ್ಟರ್}",
        "YANKEE": "YANKEE {ಯಾಂಕೀ}",
    }),
    # Skip: ASSOCIATED WITH #2 (Deputy, Derek Jeter, Pencil, Silver Medal - US/baseball specific)

    # Day 370
    "BASKETBALL SHOTS": ("BASKETBALL SHOTS {ಬ್ಯಾಸ್ಕೆಟ್‌ಬಾಲ್ ಹೊಡೆತಗಳು}", {
        "DUNK": "DUNK {ಡಂಕ್}",
        "FLOATER": "FLOATER {ಫ್ಲೋಟರ್}",
        "LAYUP": "LAYUP {ಲೇಅಪ್}",
        "THREE": "THREE {ತ್ರಿ-ಪಾಯಿಂಟರ್}",
    }),
    "FISH": ("FISH {ಮೀನಿನ ತಳಿಗಳು}", {
        "PERCH": "PERCH {ಪರ್ಚ್ ಮೀನು}",
        "PIKE": "PIKE {ಪೈಕ್ ಮೀನು}",
        "SKATE": "SKATE {ಸ್ಪ್ರೇ ಮೀನು}",
        "SOLE": "SOLE {ಸೋಲ್ ಮೀನು}",
    }),
    "QUALITIES OF THICK HAIR": ("QUALITIES OF THICK HAIR {ದಟ್ಟ ಕೂದಲಿನ ಲಕ್ಷಣಗಳು}", {
        "BODY": "BODY {ದಟ್ಟತೆ}",
        "BOUNCE": "BOUNCE {ಮಿಂಚು/ಚೈತನ್ಯ}",
        "LIFT": "LIFT {ಉಬ್ಬು}",
        "VOLUME": "VOLUME {ಗಾತ್ರ}",
    }),
    # Skip: ___ CHILD (English collocations Flower, Only, Poster, Problem)

    # Day 371
    "CURRENT SITUATION": ("CURRENT SITUATION {ಪ್ರಸ್ತುತ ಪರಿಸ್ಥಿತಿ}", {
        "CONDITION": "CONDITION {ಸ್ಥಿತಿ}",
        "FORM": "FORM {ರೂಪ}",
        "SHAPE": "SHAPE {ಆಕಾರ}",
        "STATE": "STATE {ಸ್ಥಿತಿಗತಿ}",
    }),
    "REMOTE RURAL AREA": ("REMOTE RURAL AREA {ದೂರದ ಗ್ರಾಮೀಣ ಪ್ರದೇಶ}", {
        "BUSH": "BUSH {ಕುರುಚಲು ಕಾಡು}",
        "COUNTRY": "COUNTRY {ಹಳ್ಳಿಗಾಡು}",
        "STICKS": "STICKS {ಮೂಲೆಗ್ರಾಮ}",
        "WOODS": "WOODS {ಕಾಡು ಪ್ರದೇಶ}",
    }),
    "CLASSIC LAWN ORNAMENTS": ("CLASSIC LAWN ORNAMENTS {ಉದ್ಯಾನವನದ ಅಲಂಕಾರಿಕ ವಸ್ತುಗಳು}", {
        "FLAMINGO": "FLAMINGO {ಪ್ಲಾಸ್ಟಿಕ್ ಫ್ಲೆಮಿಂಗೋ}",
        "FOUNTAIN": "FOUNTAIN {ಕಾರಂಜಿ}",
        "GNOME": "GNOME {ಕುಬ್ಜ ಗೊಂಬೆ}",
        "PINWHEEL": "PINWHEEL {ಗಾಳಿಗೆ ತಿರುಗುವ ಚಕ್ರ}",
    }),
    # Skip: ___ TALE (English collocations Fairy, Fish, Folk, Tall)

    # Day 372
    "DELIVER, AS A PACKAGE": ("DELIVER, AS A PACKAGE {ಪಾರ್ಸೆಲ್ ರವಾನಿಸುವುದು}", {
        "MAIL": "MAIL {ಅಂಚೆ ರವಾನೆ}",
        "POST": "POST {ಪೋಸ್ಟ್ ಮಾಡು}",
        "SEND": "SEND {ಕಳುಹಿಸು}",
        "SHIP": "SHIP {ಸಾಗಿಸು}",
    }),
    "KINDS OF LIP MAKEUP": ("KINDS OF LIP MAKEUP {ತುಟಿಯ ಸೌಂದರ್ಯವರ್ಧಕಗಳು}", {
        "BALM": "BALM {ಲಿಪ್ ಬಾಮ್}",
        "GLOSS": "GLOSS {ಲಿಪ್ ಗ್ಲಾಸ್}",
        "LINER": "LINER {ಲಿಪ್ ಲೈನರ್}",
        "STAIN": "STAIN {ಲಿಪ್ ಸ್ಟೇನ್}",
    }),
    "PREDICAMENT": ("PREDICAMENT {ಇಕ್ಕಟ್ಟು/ಕಷ್ಟದ ಪರಿಸ್ಥಿತಿ}", {
        "CORNER": "CORNER {ಇಕ್ಕಟ್ಟು}",
        "FIX": "FIX {ಪೇಚಾಟ}",
        "HOLE": "HOLE {ಹಳ್ಳ}",
        "SPOT": "SPOT {ಕಠಿಣ ಸಂದರ್ಭ}",
    }),
    "MEASURED IN DEGREES": ("MEASURED IN DEGREES {ಡಿಗ್ರಿಗಳಲ್ಲಿ ಅಳೆಯಲ್ಪಡುವ ವಿಷಯಗಳು}", {
        "ANGLE": "ANGLE {ಕೋನ}",
        "CRIME": "CRIME {ಅಪರಾಧದ ತೀವ್ರತೆ}",
        "EDUCATION": "EDUCATION {ಶೈಕ್ಷಣಿಕ ಪದವಿ}",
        "TEMPERATURE": "TEMPERATURE {ತಾಪಮಾನ}",
    }),

    # Day 373
    "REMOTE CONTROL BUTTONS": ("REMOTE CONTROL BUTTONS {ಟಿವಿ ರಿಮೋಟ್ ಗುಂಡಿಗಳು}", {
        "CHANNEL": "CHANNEL {ಚಾನೆಲ್}",
        "MENU": "MENU {ಮೆನು}",
        "POWER": "POWER {ಪವರ್}",
        "VOLUME": "VOLUME {ವಾಲ್ಯೂಮ್}",
    }),
    "HIDE FROM VIEW": ("HIDE FROM VIEW {ದೃಷ್ಟಿಯಿಂದ ಮರೆಮಾಡುವುದು}", {
        "BLOCK": "BLOCK {ತಡೆಗಟ್ಟು}",
        "COVER": "COVER {ಮುಚ್ಚು}",
        "SCREEN": "SCREEN {ಮರೆಮಾಡು}",
        "SHIELD": "SHIELD {ರಕ್ಷಣೆ ನೀಡು}",
    }),
    "DRINK GARNISHES": ("DRINK GARNISHES {ಪಾನೀಯ ಅಲಂಕಾರದ ವಸ್ತುಗಳು}", {
        "CHERRY": "CHERRY {ಚೆರ್ರಿ ಹಣ್ಣು}",
        "OLIVE": "OLIVE {ಆಲೀವ್ ಕಾಯಿ}",
        "SWORD": "SWORD {ಪ್ಲಾಸ್ಟಿಕ್ ಖಡ್ಗ}",
        "UMBRELLA": "UMBRELLA {ಚಿಕ್ಕ ಛತ್ರಿ}",
    }),
    "FIRST WORD IN BOND MOVIE TITLES": ("FIRST WORD IN BOND MOVIE TITLES {ಜೇಮ್ಸ್ ಬಾಂಡ್ ಚಿತ್ರಗಳ ಶೀರ್ಷಿಕೆಯ ಮೊದಲ ಪದ}", {
        "CASINO": "CASINO {ಕ್ಯಾಸಿನೋ ರಾಯಲ್}",
        "DIAMONDS": "DIAMONDS {ಡೈಮಂಡ್ಸ್ ಆರ್ ಫಾರೆವರ್}",
        "QUANTUM": "QUANTUM {ಕ್ವಾಂಟಮ್ ಆಫ್ ಸೋಲೇಸ್}",
        "TOMORROW": "TOMORROW {ಟುಮಾರೋ ನೆವರ್ ಡೈಸ್}",
    }),

    # Day 374
    "POSITIONS IN FAVOR": ("POSITIONS IN FAVOR {ಪರವಾದ ಒಲವು}", {
        "AYE": "AYE {ಒಪ್ಪಿಗೆ/ಆಯ್}",
        "FOR": "FOR {ಪರವಾಗಿ}",
        "PRO": "PRO {ಪರ}",
        "YEA": "YEA {ಹೌದು}",
    }),
    "GO OUT WITH": ("GO OUT WITH {ಜತೆಯಲ್ಲಿ ಓಡಾಡು/ಡೇಟಿಂಗ್}", {
        "COURT": "COURT {ಪ್ರೇಮ ಯಾಚಿಸು}",
        "DATE": "DATE {ಡೇಟಿಂಗ್ ಮಾಡು}",
        "SEE": "SEE {ಭೇಟಿಯಾಗು}",
        "WOO": "WOO {ಒಲಿಸಿಕೊಳ್ಳು}",
    }),
    "MULTITUDE": ("MULTITUDE {ಬೃಹತ್ ಗುಂಪು/ಸಮೂಹ}", {
        "DROVE": "DROVE {ದಂಡು}",
        "HOST": "HOST {ಅಪಾರ ಸಂಖ್ಯೆ}",
        "PACK": "PACK {ಹಿಂಡು}",
        "SEA": "SEA {ಜನಸಾಗರ}",
    }),
    "THINGS READ IN DIVINATION": ("THINGS READ IN DIVINATION {ಭವಿಷ್ಯ ಹೇಳಲು ನೋಡುವ ಸಂಗತಿಗಳು}", {
        "AURA": "AURA {ಪ್ರಭಾವಲಯ}",
        "PALM": "PALM {ಹಸ್ತಸಾಮುದ್ರಿಕ/ಅಂಗೈ}",
        "TAROT": "TAROT {ಟ್ಯಾರೋ ಕಾರ್ಡ್}",
        "TEA": "TEA {ಟೀ ಎಲೆಗಳು}",
    }),

    # Day 375
    "BITS OF HARDWARE": ("BITS OF HARDWARE {ಯಂತ್ರಾಂಶದ ಬಿಡಿಭಾಗಗಳು}", {
        "NAIL": "NAIL {ಮೊಳೆ}",
        "NUT": "NUT {ನಟ್}",
        "SCREW": "SCREW {ತಿರುಪು/ಸ್ಕ್ರೂ}",
        "WASHER": "WASHER {ವಾಷರ್}",
    }),
    "FISHING GEAR": ("FISHING GEAR {ಮೀನು ಹಿಡಿಯುವ ಉಪಕರಣಗಳು}", {
        "FLY": "FLY {ಕೃತಕ ಕೀಟದ ಗಾಳ}",
        "HOOK": "HOOK {ಕೊಕ್ಕೆ/ಗಾಳ}",
        "LINE": "LINE {ದಾರ}",
        "SINKER": "SINKER {ಸೀಸದ ತೂಕ}",
    }),
    "HAIR SALON FIXTURES": ("HAIR SALON FIXTURES {ಕ್ಷೌರದಂಗಡಿಯ ಪರಿಕರಗಳು}", {
        "CHAIR": "CHAIR {ಕುರ್ಚಿ}",
        "DRYER": "DRYER {ಡ್ರೈಯರ್}",
        "MIRROR": "MIRROR {ಕನ್ನಡಿ}",
        "SINK": "SINK {ಸಿಂಕ್}",
    }),
    # Skip: LIGHTNING ___ (English collocations Bolt, Bug, Rod, Strike)

    # Day 376
    "AMUSEMENT PARK RIDES": ("AMUSEMENT PARK RIDES {ಮನರಂಜನಾ ಪಾರ್ಕ್‌ನ ಸವಾರಿಗಳು}", {
        "FERRIS WHEEL": "FERRIS WHEEL {ದೈತ್ಯ ತಿರುಗಣೆ ತೊಟ್ಟಿಲು}",
        "MERRY-GO-ROUND": "MERRY-GO-ROUND {ಮೋಜಿನ ಕುದುರೆ ತಿರುಗಣೆ}",
        "ROLLER COASTER": "ROLLER COASTER {ರೋಲರ್ ಕೋಸ್ಟರ್}",
        "TILT-A-WHIRL": "TILT-A-WHIRL {ಟಿಲ್ಟ್-ಎ-ವರ್ಲ್}",
    }),
    "APPROVAL": ("APPROVAL {ಒಪ್ಪಿಗೆ/ಅನುಮೋದನೆ}", {
        "CLEARANCE": "CLEARANCE {ಅನುಮತಿ}",
        "GO-AHEAD": "GO-AHEAD {ಮುಂದುವರಿಯಲು ಅನುಮೋದನೆ}",
        "GREEN LIGHT": "GREEN LIGHT {ಹಸಿರು ನಿಶಾನೆ}",
        "THUMBS-UP": "THUMBS-UP {ತೋರುಬೆರಳು ಎತ್ತಿ ಒಪ್ಪಿಗೆ}",
    }),
    "TYPES OF COME-FROM-BEHIND STORIES": ("TYPES OF COME-FROM-BEHIND STORIES {ಅನಿರೀಕ್ಷಿತ ಗೆಲುವಿನ ಕಥೆಗಳು}", {
        "CINDERELLA": "CINDERELLA {ಸಿಂಡರೆಲ್ಲಾ ಕಥೆ}",
        "DAVID-AND-GOLIATH": "DAVID-AND-GOLIATH {ಡೇವಿಡ್ ಮತ್ತು ಗೋಲಿಯಾತ್}",
        "RAGS-TO-RICHES": "RAGS-TO-RICHES {ಬಡತನದಿಂದ ಸಿರಿವಂತಿಕೆ}",
        "UNDERDOG": "UNDERDOG {ಅನಿರೀಕ್ಷಿತ ವಿಜೇತ}",
    }),
    # Skip: BEGINNING WITH SYNONYMS FOR REAR END (English slang wordplay Bumper-to-Bumper, Buttermilk, Rumpelstiltskin, Tailgate)

    # Day 377
    "ONE THING AFTER ANOTHER": ("ONE THING AFTER ANOTHER {ಸರಣಿ/ಒಂದಾದ ಮೇಲೊಂದರಂತೆ}", {
        "CHAIN": "CHAIN {ಸರಪಳಿ}",
        "TRAIN": "TRAIN {ಸಾಲಾಗಿ ಬರುವುದು}",
        "SERIES": "SERIES {ಸರಣಿ}",
        "STRING": "STRING {ಮಾಲೆ}",
    }),
    "KINDS OF GOLF CLUBS": ("KINDS OF GOLF CLUBS {ಗಾಲ್ಫ್ ಬ್ಯಾಟ್ ವಿಧಗಳು}", {
        "DRIVER": "DRIVER {ಡ್ರೈವರ್}",
        "IRON": "IRON {ಐರನ್}",
        "WEDGE": "WEDGE {ವೆಡ್ಜ್}",
        "WOOD": "WOOD {ವುಡ್}",
    }),
    "HORROR MOVIES, WITH \u201cTHE\u201d": ("HORROR MOVIES, WITH \u201cTHE\u201d {ಪ್ರಸಿದ್ಧ ಹಾರರ್ ಸಿನಿಮಾಗಳು}", {
        "BIRDS": "BIRDS {ದ ಬರ್ಡ್ಸ್}",
        "FOG": "FOG {ದ ಫಾಗ್}",
        "OMEN": "OMEN {ದ ಒಮೆನ್}",
        "RING": "RING {ದ ರಿಂಗ್}",
    }),
    # Skip: WORDS FOR SAUSAGE (Western meat slang Brat, Dog, Frank, Link)

    # Day 378
    "\u201cSETTLE DOWN!\u201d": ("\u201cSETTLE DOWN!\u201d {ಶಾಂತರಾಗಿ/ಸಮಾಧಾನವಾಗಿ}", {
        "EASY": "EASY {ಸಮಾಧಾನ}",
        "ENOUGH": "ENOUGH {ಸಾಕು}",
        "RELAX": "RELAX {ವಿಶ್ರಾಂತವಾಗಿರು}",
        "QUIET": "QUIET {ಶಾಂತರಾಗಿ}",
    }),
    "MINOR AILMENTS": ("MINOR AILMENTS {ಸಣ್ಣಪುಟ್ಟ ಆರೋಗ್ಯ ಸಮಸ್ಯೆಗಳು}", {
        "BUG": "BUG {ವೈರಲ್ ಜ್ವರ}",
        "CHILL": "CHILL {ಚಳಿ}",
        "COLD": "COLD {ಶೀತ}",
        "COUGH": "COUGH {ಕೆಮ್ಮು}",
    }),
    "WHAT HUMPBACK WHALES DO": ("WHAT HUMPBACK WHALES DO {ತಿಮಿಂಗಿಲಗಳ ಚಟುವಟಿಕೆಗಳು}", {
        "BREACH": "BREACH {ನೀರಿನಿಂದ ಜಿಗಿಯುವುದು}",
        "DIVE": "DIVE {ಮುಳುಗು ಹಾಕುವುದು}",
        "SING": "SING {ಹಾಡುವುದು}",
        "SPOUT": "SPOUT {ನೀರು ಚಿಮ್ಮಿಸುವುದು}",
    }),
    # Skip: ___ CITY NICKNAMES (Magic, Motor, Sin, Windy - US city nicknames)
}


def process_chunk():
    kannada_path = r'C:\Users\anilg\development\My Projects\vibecoding\word_puzzles\connections\kannada_connections.json'
    connections_path = r'C:\Users\anilg\development\My Projects\vibecoding\word_puzzles\connections\connections.json'
    readme_path = r'C:\Users\anilg\development\My Projects\vibecoding\word_puzzles\connections\Connections_README.md'

    with open(kannada_path, 'r', encoding='utf-8') as f:
        kannada_data = json.load(f)
    with open(connections_path, 'r', encoding='utf-8') as f:
        conn_data = json.load(f)

    start_idx = len(kannada_data)
    end_idx = min(start_idx + 18, len(conn_data))
    chunk = conn_data[start_idx:end_idx]

    print(f"Processing chunk [{start_idx}:{end_idx}] (Days {start_idx + 1} to {end_idx})...")

    adapted_chunk = []
    adapted_count = 0
    skipped_count = 0

    for day in chunk:
        day_copy = {
            "id": day.get("id"),
            "date": day["date"],
            "answers": []
        }
        for ans in day["answers"]:
            orig_group = ans["group"]
            orig_members = ans["members"]
            level = ans["level"]

            if orig_group in MAPPINGS:
                new_group, member_map = MAPPINGS[orig_group]
                new_members = [member_map.get(m, m) for m in orig_members]
                day_copy["answers"].append({
                    "level": level,
                    "group": new_group,
                    "members": new_members
                })
                adapted_count += 1
            else:
                day_copy["answers"].append({
                    "level": level,
                    "group": orig_group,
                    "members": list(orig_members)
                })
                skipped_count += 1

        adapted_chunk.append(day_copy)

    kannada_data.extend(adapted_chunk)

    with open(kannada_path, 'w', encoding='utf-8') as f:
        json.dump(kannada_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully appended {len(adapted_chunk)} days!")
    print(f"Total days now in kannada_connections.json: {len(kannada_data)}")
    print(f"Groups adapted: {adapted_count}, Groups skipped: {skipped_count}")

    # Update Connections_README.md
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    import re
    readme_content = re.sub(
        r"\* \*\*Progress Checkpoint\*\*.*",
        f"* **Progress Checkpoint**: We have successfully processed **Days 1 through {end_idx}** (total {len(kannada_data)} days).",
        readme_content
    )
    readme_content = re.sub(
        r"\* \*\*Next Action\*\*.*",
        f"* **Next Action**: The next AI session should resume from **Day {end_idx + 1}** (using list slicing `data[{end_idx}:{end_idx + 18}]` in Python for the next chunk).",
        readme_content
    )

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print("Updated Connections_README.md with new progress checkpoint.")

if __name__ == '__main__':
    process_chunk()
