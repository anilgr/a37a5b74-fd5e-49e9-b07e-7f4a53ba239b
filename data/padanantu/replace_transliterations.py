import json
import re

replacements = {
    # PASTA SHAPES (adapt to local snacks/shapes)
    "BOWTIE {ಬೋ}": "BOWTIE {ಚಕ್ಕುಲಿ}",
    "ELBOW {ಎಲ್ಬೋ}": "ELBOW {ಕೋಡುಬಳೆ}",
    "ELBOW {ಕೊಳವೆ}": "ELBOW {ಕೋಡುಬಳೆ}",
    "SHELL {ಶಂಖ}": "SHELL {ನಿಪ್ಪಟ್ಟು}",
    "SPIRAL {ಸುರುಳಿ}": "SPIRAL {ಮುರುಕು}",

    # DOG BREEDS
    "BOXER {ಬಾಕ್ಸರ್/ಡಾಬರ್‌ಮನ್}": "BOXER {ಮುಧೋಳ}",
    "DALMATIAN {ಡಾಲ್ಮೇಷಿಯನ್/ಪಗ್}": "DALMATIAN {ರಾಜಪಾಳ್ಯಂ}",
    "HUSKY {ಹಸ್ಕಿ}": "HUSKY {ಕನ್ನಿ}",
    "POODLE {ಪೂಡಲ್/ಲ್ಯಾಬ್ರಡಾರ್}": "POODLE {ಚಿಪ್ಪಿಪಾರೈ}",

    # EUROPEAN COUNTRIES
    "DENMARK {ಡೆನ್ಮಾರ್ಕ್}": "DENMARK {ಕರ್ನಾಟಕ}",
    "GREECE {ಗ್ರೀಸ್}": "GREECE {ಕೇರಳ}",
    "POLAND {ಪೋಲೆಂಡ್}": "POLAND {ಮಹಾರಾಷ್ಟ್ರ}",
    "PORTUGAL {ಪೋರ್ಚುಗಲ್}": "PORTUGAL {ತಮಿಳುನಾಡು}",

    # ISLAND COUNTRIES
    "CUBA {ಕ್ಯೂಬಾ}": "CUBA {ಸೇಂಟ್ ಮೇರಿಸ್ ದ್ವೀಪ}",
    "JAPAN {ಜಪಾನ್}": "JAPAN {ನೇತ್ರಾಣಿ ದ್ವೀಪ}",
    "MALTA {ಮಾಲ್ಟಾ}": "MALTA {ಕುರುಮಗಡ}",
    "PALAU {ಪಲಾವ್}": "PALAU {ಬಸವರಾಜ ದುರ್ಗ}",
    "TUNISIA {ಟುನೀಶಿಯಾ}": "TUNISIA {ಲಕ್ಷದ್ವೀಪ}",
    "TURKEY {ಟರ್ಕಿ}": "TURKEY {ಅಂಡಮಾನ್}",

    # FLIGHTLESS BIRDS
    "EMU {ಈಮು}": "EMU {ನವಿಲು}",
    "KIWI {ಕಿವಿ}": "KIWI {ಮರಕುಟಿಗ}",
    "OSTRICH {ಉಷ್ಟ್ರಪಕ್ಷಿ}": "OSTRICH {ಗರಗಸ ಹಕ್ಕಿ}",
    "PENGUIN {ಪೆಂಗ್ವಿನ್}": "PENGUIN {ಗೀಜಗ}",

    # MUSIC GENRES
    "JAZZ {ಜಾಝ್/ಶಾಸ್ತ್ರೀಯ}": "JAZZ {ಶಾಸ್ತ್ರೀಯ}",
    "POP {ಪಾಪ್}": "POP {ಭಾವಗೀತೆ}",
    "PUNK {ಪಂಕ್/ಜಾನಪದ}": "PUNK {ಜಾನಪದ}",
    "RAP {ರ್ಯಾಪ್}": "RAP {ಸುಗಮ ಸಂಗೀತ}",

    # SODA BRANDS
    "CRUSH {ಮಜಾ}": "CRUSH {ಬೋಂಟಾ}",
    "MUG {ಥಮ್ಸ್ ಅಪ್}": "MUG {ಪನ್ನೀರ್ ಸೋಡಾ}",
    "SPRITE {ಸ್ಪ್ರೈಟ್}": "SPRITE {ಜೀರಾ ಮಸಾಲ}",
    "SQUIRT {ಫ್ಯಾಂಟಾ}": "SQUIRT {ಗೋಲಿ ಸೋಡಾ}",

    # EXTINCT ANIMALS
    "DODO {ಡೋಡೋ}": "DODO {ಗಂಡಭೇರುಂಡ}",
    "MAMMOTH {ಮ್ಯಾಮತ್}": "MAMMOTH {ಮಕರ}",
    "MASTODON {ಮಾಸ್ಟೋಡಾನ್}": "MASTODON {ಯಾಳಿ}",
    "TRILOBITE {ಟ್ರೈಲೋಬೈಟ್}": "TRILOBITE {ಶರಭ}",

    # FABRICS
    "CORDUROY {ರೇಷ್ಮೆ}": "CORDUROY {ರೇಷ್ಮೆ}",
    "DENIM {ಡೆನಿಮ್}": "DENIM {ಖಾದಿ}",
    "LINEN {ಲಿನೆನ್}": "LINEN {ಇಳಕಲ್}",
    "TWEED {ಹತ್ತಿ}": "TWEED {ಮೈಸೂರು ಸಿಲ್ಕ್}",

    # CAR BRANDS
    "MINI {ಮಿನಿ}": "MINI {ಅಶೋಕ್ ಲೇಲ್ಯಾಂಡ್}",
    "RAM {ರಾಮ್}": "RAM {ಐಷರ್}",
    "SUBARU {ಸುಬಾರು}": "SUBARU {ಫೋರ್ಸ್}",

    # SPORTS VENUES
    "COURT {ಕೋರ್ಟ್}": "COURT {ಮೈದಾನ}",
    "FIELD {ಫೀಲ್ಡ್}": "FIELD {ಕ್ರೀಡಾಂಗಣ}",
    
    # WINE TASTING DESCRIPTORS -> Coffee Descriptors
    "DRY {ಡ್ರೈ}": "DRY {ಕಡು}",
    "FULL {ಫುಲ್}": "FULL {ಸ್ಟ್ರಾಂಗ್‌}",
    
    # APPETIZER UNIT
    "FRY {ಫ್ರೈ}": "FRY {ಬೋಂಡ}",
    "WING {ವಿಂಗ್ಸ್}": "WING {ಪಕೋಡ}",

    # MAC KEYBOARD KEYS
    "SHIFT {ಶಿಫ್ಟ್}": "SHIFT {ಶಿಫ್ಟ್}",

    # ITALIAN DEMONYMS -> local districts
    "BOLOGNESE {ಬೊಲೊಗ್ನೀಸ್}": "BOLOGNESE {ಮೈಸೂರು}",
    "PARMESAN {ಪಾರ್ಮಿಸನ್}": "PARMESAN {ಧಾರವಾಡ}",
    "MARINARA {ಮರಿನಾರಾ}": "MARINARA {ಕಾಯಿ ಚಟ್ನಿ}",

    # RODENTS
    "GERBIL {ಹೆಗ್ಗಣ}": "GERBIL {ಹೆಗ್ಗಣ}",
    "HAMSTER {ಹ್ಯಾಮ್ಸ್ಟರ್}": "HAMSTER {ಅಳಿಲು}",
    "RAT {ಇಲಿ}": "RAT {ಇಲಿ}",
    "VOLE {ವೋಲ್}": "VOLE {ಮುಂಗುಸಿ}",

    # MUPPETS
    "ANIMAL {ಅನಿಮಲ್}": "ANIMAL {ಗೊಂಬೆ}",
    "BEAKER {ಬೀಕರ್}": "BEAKER {ಸೂತ್ರದ ಬೊಂಬೆ}",

    # ART MOVEMENTS
    "DADA {ದಾದಾ}": "DADA {ಚಿತ್ತಾರ}",
    # POP is already covered

    # FOOTWEAR
    "BOOT {ಬೂಟು}": "BOOT {ಮೊಜರಿ}",
    "LOAFER {ಶೂ}": "LOAFER {ಶೂ}",
    "PUMP {ಸ್ಯಾಂಡಲ್}": "PUMP {ಕೋಲಾಪುರಿ}",
    "SNEAKER {ಚಪ್ಪಲಿ}": "SNEAKER {ಚಪ್ಪಲಿ}",
    
    "BOOT {ಬೂಟ್}": "BOOT {ಮೊಜರಿ}",

    # SHADES OF BLACK
    "EBONY {ಎಬೊನಿ}": "EBONY {ಕಾರ್ಮೋಡ}",
    "JET {ಕಡುಗಪ್ಪು}": "JET {ಕಡುಗಪ್ಪು}",
    "ONYX {ಕಾಡಿಗೆ}": "ONYX {ಕಾಡಿಗೆ}",
    "RAVEN {ರೇವನ್}": "RAVEN {ಕಾಗೆ}",

    # DANCE MOVES
    "FLOSS {ಫ್ಲಾಸ್}": "FLOSS {ಡೊಳ್ಳು ಕುಣಿತ}",
    "ROBOT {ರೋಬೋಟ್}": "ROBOT {ಕಂಸಾಳೆ}",
    "VOGUE {ವೋಗ್}": "VOGUE {ಯಕ್ಷಗಾನ}",

    # PLAYGROUND FIXTURES
    "SEESAW {ಸೀಸಾ}": "SEESAW {ಗರಗಸ ಆಟ}",

    # GOLF TERMS
    "DRIVER {ಡ್ರೈವರ್}": "DRIVER {ದಾಂಡು}",
    "EAGLE {ಹದ್ದಿನಗುರಿ}": "EAGLE {ಹದ್ದಿನಗುರಿ}",
    "HOLE {ಗುಂಡಿ}": "HOLE {ಗುಂಡಿ}",
    "STROKE {ಸ್ಟ್ರೋಕ್}": "STROKE {ಹೊಡೆತ}",

    # ANIMALS WITH TUSKS
    "NARWHAL {ನಾರ್ವಾಲ್}": "NARWHAL {ಖಡ್ಗಮೃಗ}",
    
    # ROMANTIC BEGINNINGS
    "SPARK {ಸ್ಪಾರ್ಕ್}": "SPARK {ಮಿಂಚು}",
    "VIBE {ವೈಬ್}": "VIBE {ಒಲವು}",
    
    # CATCHY SONG
    "BOP {ಬಾಪ್}": "BOP {ಹಾಡು}",
    "GROOVE {ಗ್ರೂವ್}": "GROOVE {ತಾಳ}",
    "JAM {ಜಾಮ್}": "JAM {ರಾಗ}",

    # FUNNY PERSON
    "JOKER {ಜೋಕರ್}": "JOKER {ವಿದೂಷಕ}",
    
    # U.S.-BASED AIRLINES
    "SPIRIT {ಸ್ಪಿರಿಟ್}": "SPIRIT {ಇಂಡಿಗೋ}",
    "UNITED {ಯುನೈಟೆಡ್}": "UNITED {ಸ್ಪೈಸ್‌ಜೆಟ್}",
    
    # WEB BROWSERS
    "OPERA {ಒಪೇರಾ}": "OPERA {ಒಪೇರಾ}",
    "SAFARI {ಸಫಾರಿ}": "SAFARI {ಸಫಾರಿ}",

    # DETERGENTS
    "TIDE {ಟೈಡ್}": "TIDE {ವೀಲ್}",
    "ALL {ಸರ್ಫ್ ಎಕ್ಸೆಲ್}": "ALL {ಸರ್ಫ್ ಎಕ್ಸೆಲ್}",
    "ERA {ರಿನ್}": "ERA {ರಿನ್}",
    "GAIN {ಏರಿಯಲ್}": "GAIN {ಏರಿಯಲ್}",

    # EAR PARTS
    "ANVIL {ಅನ್ವಿಲ್}": "ANVIL {ಕಿವಿಯ ಮೂಳೆ}",

    # MARINE MAMMALS
    "MANATEE {ಮನಾಟಿ}": "MANATEE {ನೀರುಹಂದಿ}",
    "SEAL {ಸೀಲ್}": "SEAL {ಸೀಲ್}",

    # BIKE PARTS
    "BRAKE {ಬ್ರೇಕ್}": "BRAKE {ತಡೆಯು}",
    "CHAIN {ಚೈನ್}": "CHAIN {ಸರಪಳಿ}",
    "SPOKE {ಸ್ಪೋಕ್ಸ್}": "SPOKE {ಕಡ್ಡಿ}",
    "GEAR {ಗೇರ್}": "GEAR {ಗೇರ್}",
    "PEDAL {ಪೆಡಲ್}": "PEDAL {ಪೆಡಲ್}",
    
    # HAIRSTYLES
    "BOB {ಬಾಬ್}": "BOB {ಬಾಬ್}",
    
    # STORMS
    "TORNADO {ಟೊರ್ನಾಡೊ}": "TORNADO {ಸುಂಟರಗಾಳಿ}",
    
    # COMPUTER EQUIPMENT
    "MONITOR {ಮಾನಿಟರ್}": "MONITOR {ಪರದೆ}",
    "MOUSE {ಮೌಸ್}": "MOUSE {ಮೌಸ್}",
    "SPEAKER {ಸ್ಪೀಕರ್}": "SPEAKER {ಧ್ವನಿವರ್ಧಕ}",

    # FISH
    "SHARK {ಶಾರ್ಕ್}": "SHARK {ಸುರೈ}",
    
    # THEORETICAL PHYSICISTS
    "EINSTEIN {ಐನ್‌ಸ್ಟೈನ್}": "EINSTEIN {ಸಿ.ವಿ. ರಾಮನ್}",
    "OPPENHEIMER {ಓಪನ್‌ಹೈಮರ್}": "OPPENHEIMER {ಹೋಮಿ ಭಾಭಾ}",
    "FEYNMAN {ಫೈನ್‌ಮನ್}": "FEYNMAN {ಸತ್ಯೇಂದ್ರ ನಾಥ ಬೋಸ್}",
    "HAWKING {ಹಾಕಿಂಗ್}": "HAWKING {ಸುಬ್ರಹ್ಮಣ್ಯನ್ ಚಂದ್ರಶೇಖರ್}",

    # GYM EXERCISES
    "PRESS {ಪ್ರೆಸ್}": "PRESS {ಒತ್ತು}",
    "CURL {ಕರ್ಲ್}": "CURL {ಸುರುಳಿ}",
    "LUNGE {ಲಂಜ್}": "LUNGE {ಲಂಜ್}",
    "PLANK {ಪ್ಲಾಂಕ್}": "PLANK {ಪ್ಲಾಂಕ್}",

    # FACIAL HAIR
    "MUSTACHE {ಮೀಸೆ}": "MUSTACHE {ಮೀಸೆ}",

    # FAILURES
    "FLOPS {ಫ್ಲಾಪ್}": "FLOPS {ಸೋಲು}",
    "FLOP {ಫ್ಲಾಪ್}": "FLOP {ಸೋಲು}",

    # AUTOMATIC TRANSMISSION SETTINGS
    "DRIVE {ಡ್ರೈವ್}": "DRIVE {ಚಲಾಯಿಸು}",
    "PARK {ಪಾರ್ಕ್}": "PARK {ನಿಲ್ಲಿಸು}",
    "REVERSE {ರಿವರ್ಸ್}": "REVERSE {ಹಿಂದಕ್ಕೆ}",

    # SLOT MACHINE SYMBOLS
    "BAR {ಬಾರ್}": "BAR {ಬಾರ್}",
    "CHERRY {ಚೆರ್ರಿ}": "CHERRY {ಹಣ್ಣು}",

    # GYMNASTICS APPARATUS
    "FLOOR {ಫ್ಲೋರ್}": "FLOOR {ನೆಲ}",
    "HORSE {ಹಾರ್ಸ್}": "HORSE {ಕುದುರೆ}",
    "VAULT {ವಾಲ್ಟ್}": "VAULT {ಜಿಗಿತ}",
    
    # WESTERN TROPES
    "SHERIFF {ಶೆರಿಫ್}": "SHERIFF {ಗೌಡ}",
    
    # BOWLING
    "ALLEY {ಆಲಿ}": "ALLEY {ಗಲ್ಲಿ}",
    "LANE {ಲೇನ್}": "LANE {ಪಥ}",
    "PIN {ಪಿನ್}": "PIN {ಮೊಳೆ}",
    
    # COMMON SWAG ITEMS
    "MUG {ಮಗ್}": "MUG {ಲೋಟ}",
    
    # SUPER MARIO-RELATED
    "DINOSAUR {ಡೈನೋಸಾರ್}": "DINOSAUR {ಬೆಕ್ಕಿನ ಮರಿ}",
    "PLUMBER {ಪ್ಲಂಬರ್}": "PLUMBER {ನೀರುಗಂಟಿ}",
    
    # LINGERIE
    "GARTER {ಗಾರ್ಟರ್}": "GARTER {ನಾರು}",
    "SLIP {ಸ್ಲಿಪ್}": "SLIP {ಒಳಲಂಗ}",
    "TEDDY {ಟೆಡ್ಡಿ}": "TEDDY {ಟೆಡ್ಡಿ}",

    # PLAYING CARD SUITS
    "HEART {ಹಾರ್ಟ್}": "HEART {ಚೌಕಟ್ಟು}",
    "SPADE {ಸ್ಪೇಡ್}": "SPADE {ಕಳಾವರ}",
    
    # TORUS-SHAPED FOOD
    "DONUT {ಡೋನಟ್}": "DONUT {ಕೋಡುಬಳೆ}",

    # LAUGHTER, IN A TEXT
    "DEAD {ಡೆಡ್}": "DEAD {ಡೆಡ್}",
    "HAHA {ಹಹಾ}": "HAHA {ಹಹಾ}",
    "LOL {ಲಾಲ್}": "LOL {ನಗು}",
    "ROFL {ರೋಫ್ಲ್}": "ROFL {ಬಿದ್ದು ಬಿದ್ದು ನಗು}",

    # “PETER PAN” CHARACTERS
    "HOOK {ಹುಕ್}": "HOOK {ಮದಕರಿ ನಾಯಕ}",
    "NANA {ನಾನಾ}": "NANA {ಕಿತ್ತೂರು ಚೆನ್ನಮ್ಮ}",
    "PETER {ಪೀಟರ್}": "PETER {ಸಂಗೊಳ್ಳಿ ರಾಯಣ್ಣ}",

    # ACRONYMS
    "LASER {ಲೇಸರ್}": "LASER {ಲೇಸರ್}",
    "RADAR {ರಾಡಾರ್}": "RADAR {ರಾಡಾರ್}",
    
    # CELL PHONE MODES
    "VIBRATE {ವೈಬ್ರೇಟ್}": "VIBRATE {ಕಂಪನ}",
    
    # FILMMAKING EQUIPMENT
    "BOOM {ಬೂಮ್}": "BOOM {ಬೂಮ್}",
    "DOLLY {ಡಾಲಿ}": "DOLLY {ಗಾಲಿಯ ಬಂಡಿ}",
    "LENS {ಲೆನ್ಸ್}": "LENS {ಮಸೂರ}",
    "TRIPOD {ಟ್ರೈಪಾಡ್}": "TRIPOD {ಮುಕ್ಕಾಲಿ}",
    
    # EMAIL SIGN-OFFS
    "BEST {ಬೆಸ್ಟ್}": "BEST {ಶುಭಾಶಯ}",
    "CHEERS {ಚೀರ್ಸ್}": "CHEERS {ವಂದನೆಗಳು}",
    
    # FASHIONABLE
    "HIP {ಹಿಪ್}": "HIP {ಹೊಸ ಶೈಲಿ}",
    
    # CRITICIZE
    "ROAST {ರೋಸ್ಟ್}": "ROAST {ಕಾಲೆಳೆ}",
    "SLAM {ಸ್ಲಾಮ್}": "SLAM {ಹಂಗಿಸು}",
    "BLAST {ಬ್ಲಾಸ್ಟ್}": "BLAST {ಛೀಮಾರಿ ಹಾಕು}",
    "TRASH {ಟ್ರಾಶ್}": "TRASH {ನಿಂದಿಸು}",
    
    # LAND SURROUNDED BY WATER
    "ATOLL {ಅಟಾಲ್}": "ATOLL {ಹವಳದ ದಿಬ್ಬ}",
    "KEY {ಕೀ}": "KEY {ಕಿರು ದ್ವೀಪ}",
    
    # SWINDLER
    "SHARK {ಶಾರ್ಕ್}": "SHARK {ಮೋಸಗಾರ}",

    # ACCESSORIES
    "BELT {ಬೆಲ್ಟ್}": "BELT {ನಡುಪಟ್ಟಿ}",
    
    # COMEDIAN’S OUTPUT
    "ROUTINE {ರೊಟೀನ್}": "ROUTINE {ಕಾರ್ಯಕ್ರಮ}",
    
    # ART MEDIUMS
    "PASTEL {ಪಾಸ್ಟಲ್}": "PASTEL {ಬಣ್ಣದ ಕಡ್ಡಿ}",
    
    # PARTS OF A CAR
    "BUMPER {ಬಂಪರ್}": "BUMPER {ಬಂಪರ್}",
    "HOOD {ಹುಡ್}": "HOOD {ಮುಚ್ಚಳ}",
    "TIRE {ಟೈರ್}": "TIRE {ಗಾಲಿ}",

    # BASEBALL STATS
    "DOUBLE {ಡಬಲ್}": "DOUBLE {ಎರಡು ರನ್}",

    # HIDDEN LISTENING DEVICES
    "BUG {ಬಗ್}": "BUG {ಗುಪ್ತ ಮೈಕ್}",
    "MIKE {ಮೈಕ್}": "MIKE {ಮೈಕ್}",
    
    # DO SOME MARKETING FOR
    "PLUG {ಪ್ಲಗ್}": "PLUG {ಪ್ರಚಾರ ಮಾಡು}",
    "PROMOTE {ಪ್ರಮೋಟ್}": "PROMOTE {ಪ್ರಮೋಟ್ ಮಾಡು}",

    # TENNIS SCORING TERMS
    "AD {ಆಡ್}": "AD {ಆಡ್}",
    "ALL {ಆಲ್}": "ALL {ಸಮ}",
    "LOVE {ಲವ್}": "LOVE {ಶೂನ್ಯ}",

    # "GIVE ME A BREAK!"
    "LORD {ಲಾರ್ಡ್}": "LORD {ದೇವರೇ}",
    "SHEESH {ಶೀಶ್}": "SHEESH {ಅಬ್ಬಾ}",
    
    # MUSIC PLAYER BUTTONS
    "SKIP {ಸ್ಕಿಪ್}": "SKIP {ಮುಂದೆ ಹೋಗು}",

    # CAPTAINS
    "MORGAN {ಮಾರ್ಗನ್}": "MORGAN {ಮಾರ್ಗನ್}",
    "NEMO {ನೆಮೊ}": "NEMO {ನೆಮೊ}",

    # COSTUMES WITH STRIPED SHIRTS
    "MIME {ಮೈಮ್}": "MIME {ಮೂಕಾಭಿನಯ}",
    "REFEREE {ರೆಫರಿ}": "REFEREE {ತೀರ್ಪುಗಾರ}",
    "REFEREE {ರೆಫ್ರಿ}": "REFEREE {ತೀರ್ಪುಗಾರ}",

    # COMFY SHOES
    "LOAFER {ಲೋಫರ್}": "LOAFER {ಮೆತ್ತನೆ ಶೂ}",
    "SLIPPER {ಸ್ಲಿಪ್ಪರ್}": "SLIPPER {ಚಪ್ಪಲಿ}",
    
    # MEDIA ATTENTION
    "PRESS {ಪ್ರೆಸ್}": "PRESS {ಮಾಧ್ಯಮ}",

    # INGREDIENTS IN MINESTRONE
    "BEANS {ಬೀನ್ಸ್}": "BEANS {ಹುರುಳಿಕಾಯಿ}",
    "PASTA {ಪಾಸ್ತಾ}": "PASTA {ಶಾವಿಗೆ}",

    # WALK HEAVILY
    "STOMP {ಸ್ಟಾಂಪ್}": "STOMP {ಹೆಜ್ಜೆ ಹಾಕು}",

    # '80S FASHION TRENDS
    "MULLET {ಮಲ್ಲೆಟ್}": "MULLET {ಹಿಂಬದಿ ಕೂದಲು}",

    # GYMNASTICS POSITIONS
    "PIKE {ಪೈಕ್}": "PIKE {ಬಾಗಿಕೊಳ್ಳು}",
    "SPLIT {ಸ್ಪ್ಲಿಟ್}": "SPLIT {ಕಾಲು ಚಾಚು}",
    
    # KINDS OF HEELS
    "STILETTO {ಸ್ಟಿಲೆಟೊ}": "STILETTO {ಚೂಪು ಹಿಮ್ಮಡಿ}",

    # THINGS A DOG CAN FETCH
    "FRISBEE {ಫ್ರಿಸ್ಬೀ}": "FRISBEE {ಹಾರುವ ತಟ್ಟೆ}",

    # NOTABLE TV EPISODES
    "FINALE {ಫಿನಾಲೆ}": "FINALE {ಅಂತಿಮ ಸಂಚಿಕೆ}",
    "PILOT {ಪೈಲಟ್}": "PILOT {ಮೊದಲ ಸಂಚಿಕೆ}",

    # SEEN AT A SPORTS STADIUM
    "ASTROTURF {ಆಸ್ಟ್ರೋಟರ್ಫ್}": "ASTROTURF {ಕೃತಕ ಹುಲ್ಲು}",
    "JUMBOTRON {ಜಂಬೋಟ್ರಾನ್}": "JUMBOTRON {ದೊಡ್ಡ ಪರದೆ}",

    # ONE FLYING AN AIRPLANE
    "PILOT {ಪೈಲಟ್}": "PILOT {ವಿಮಾನ ಚಾಲಕ}",
    
    # DISNEY CHARACTERS
    "DAISY {ಡೈಸಿ}": "DAISY {ಡೈಸಿ}",
    "GOOFY {ಗೂಫಿ}": "GOOFY {ಗೂಫಿ}",

    # PRESERVES, AS MEAT
    "SALTS {ಸಾಲ್ಟ್ಸ್}": "SALTS {ಉಪ್ಪು ಹಾಕು}",

    # SEEN IN “CINDERELLA”
    "SLIPPER {ಸ್ಲಿಪ್ಪರ್}": "SLIPPER {ಗಾಜಿನ ಚಪ್ಪಲಿ}",

    # WAYS TO PREPARE EGGS
    "POACH {ಪೋಚ್}": "POACH {ಬೇಯಿಸು}",

    # SECOND WORDS IN TARANTINO MOVIES
    "UNCHAINED {ಅನ್‌ಚೈನ್ಡ್}": "UNCHAINED {ಅನ್‌ಚೈನ್ಡ್}",

    # AUGMENTATIVE PREFIXES
    "SUPER {ಸೂಪರ್}": "SUPER {ಸೂಪರ್}",
    "UBER {ಉಬರ್}": "UBER {ಉಬರ್}",
    "ULTRA {ಅಲ್ಟ್ರಾ}": "ULTRA {ಅಲ್ಟ್ರಾ}",

    # BECOME LARGER
    "MUSHROOM {ಮಶ್ರೂಮ್}": "MUSHROOM {ಅಣಬೆ}",

    # FILM DEPARTMENTS
    "MAKEUP {ಮೇಕಪ್}": "MAKEUP {ಬಣ್ಣ ಬಳಿಯುವುದು}",
    "PROPS {ಪ್ರಾಪ್ಸ್}": "PROPS {ಪರಿಕರಗಳು}",
    
    # INVENT AS YOU GO
    "AD-LIB {ಆಡ್-ಲಿಬ್}": "AD-LIB {ತತ್‌ಕ್ಷಣದ ಮಾತು}",
    "IMPROV {ಇಂಪ್ರೊವ್}": "IMPROV {ಸಿದ್ಧತೆಯಿಲ್ಲದ}",

    # METRIC PREFIXES
    "KILO {ಕಿಲೋ}": "KILO {ಕಿಲೋ}",
    "MEGA {ಮೆಗಾ}": "MEGA {ಮೆಗಾ}",

    # LAB EQUIPMENT
    "BEAKER {ಬೀಕರ್}": "BEAKER {ಗಾಜಿನ ಪಾತ್ರೆ}",
    "GOGGLES {ಗಾಗಲ್ಸ್}": "GOGGLES {ಕನ್ನಡಕ}",

    # SPREADSHEET TERMS
    "FORMULA {ಫಾರ್ಮುಲಾ}": "FORMULA {ಸೂತ್ರ}"
}

with open('C:/Users/anilg/development/My Projects/vibecoding/word_puzzles/connections/kannada_connections.json', 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(f'"{old}"', f'"{new}"')

# Also replace groups if any of them are still English, maybe we don't need to but just in case.
group_replacements = {
    # If there are any western group names that were entirely left as english, it's out of scope unless we have them. 
    # The instructions say "identify instances where western concepts (like specific foods, sports, animals, places, etc.) were merely transliterated instead of culturally adapted, and apply better local Kannada adaptations to them."
    "EUROPEAN COUNTRIES {ಯುರೋಪಿಯನ್ ದೇಶಗಳು}": "SOUTH INDIAN STATES {ದಕ್ಷಿಣ ಭಾರತದ ರಾಜ್ಯಗಳು}",
    "FLIGHTLESS BIRDS {ಹಾರಲಾಗದ ಪಕ್ಷಿಗಳು}": "LOCAL BIRDS {ಸ್ಥಳೀಯ ಪಕ್ಷಿಗಳು}",
    "DOG BREEDS {ನಾಯಿ ತಳಿಗಳು}": "LOCAL DOG BREEDS {ಸ್ಥಳೀಯ ನಾಯಿ ತಳಿಗಳು}",
    "ISLAND COUNTRIES {ದ್ವೀಪ ರಾಷ್ಟ್ರಗಳು}": "LOCAL ISLANDS {ಸ್ಥಳೀಯ ದ್ವೀಪಗಳು}",
    "MUSIC GENRES {ಸಂಗೀತ ಪ್ರಕಾರಗಳು}": "LOCAL MUSIC GENRES {ಸ್ಥಳೀಯ ಸಂಗೀತ ಪ್ರಕಾರಗಳು}",
    "SODA BRANDS {ತಂಪು ಪಾನೀಯಗಳು}": "LOCAL SODA BRANDS {ಸ್ಥಳೀಯ ತಂಪು ಪಾನೀಯಗಳು}",
    "EXTINCT ANIMALS {ಅಳಿದುಹೋದ ಪ್ರಾಣಿಗಳು}": "MYTHICAL CREATURES {ಪೌರಾಣಿಕ ಪ್ರಾಣಿಗಳು}",
    "FABRICS {ಬಟ್ಟೆಯ ಪ್ರಕಾರಗಳು}": "LOCAL FABRICS {ಸ್ಥಳೀಯ ಬಟ್ಟೆಗಳು}",
    "CAR BRANDS {ಕಾರು ಬ್ರಾಂಡ್‌ಗಳು}": "INDIAN VEHICLE BRANDS {ಭಾರತೀಯ ವಾಹನ ಬ್ರಾಂಡ್‌ಗಳು}"
}

for old, new in group_replacements.items():
    content = content.replace(f'"{old}"', f'"{new}"')

with open('C:/Users/anilg/development/My Projects/vibecoding/word_puzzles/connections/kannada_connections.json', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
