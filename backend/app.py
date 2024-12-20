from flask import Flask, request, jsonify
from ml_logic import Mediator, MachinePlayer


from flask_cors import CORS

app = Flask(__name__)

CORS(app)

words = [
        "aback", "abase", "abate", "abbey", "abbot", "abhor", "abide", "abled", "abode", "abort",
        "about", "above", "abuse", "abyss", "acorn", "acrid", "actor", "acute", "adage", "adapt",
        "bacon", "badge", "badly", "bagel", "baggy", "baker", "baler", "balmy", "banal", "banjo",
        "barge", "baron", "basal", "basic", "basil", "basin", "basis", "baste", "batch", "bathe",
        "baton", "batty", "bawdy", "bayou", "beach", "beady", "beard", "beast", "beech", "beefy",
        "befit", "began", "begat", "beget", "begin", "begun", "being", "belch", "belie", "belle",
        "belly", "below", "bench", "beret", "berry", "berth", "beset", "betel", "bevel", "bezel",
        "bible", "bicep", "biddy", "bigot", "bilge", "billy", "binge", "bingo", "biome", "birch",
        "birth", "bison", "bitty", "black", "blade", "blame", "bland", "blank", "blare", "blast",
        "blaze", "bleak", "bleat", "bleed", "bleep", "blend", "bless", "blimp", "blind", "blink",
        "bliss", "blitz", "bloat", "block", "bloke", "blond", "blood", "bloom", "blown", "bluer",
        "bluff", "blunt", "blurb", "blurt", "blush", "board", "boast", "bobby", "boney", "bongo",
        "bonus", "booby", "boost", "booth", "booty", "booze", "boozy", "borax", "borne", "bosom",
        "bossy", "botch", "bough", "boule", "bound", "bowel", "boxer", "brace", "braid", "brain",
        "brake", "brand", "brash", "brass", "brave", "bravo", "brawl", "brawn", "bread", "break",
        "breed", "briar", "bribe", "brick", "bride", "brief", "brine", "bring", "brink", "briny",
        "brisk", "broad", "broil", "broke", "brood", "brook", "broom", "broth", "brown", "brunt",
        "brush", "brute", "buddy", "budge", "buggy", "bugle", "build", "built", "bulge", "bulky",
        "bully", "bunch", "bunny", "burly", "burnt", "burst", "bused", "bushy", "butch", "butte",
        "buxom", "buyer", "bylaw", "cabal", "cabby", "cabin", "cable", "cacao", "cache", "cacti",
        "caddy", "cadet", "cagey", "cairn", "camel", "cameo", "canal", "candy", "canny", "canoe",
        "canon", "caper", "caput", "carat", "cargo", "carol", "carry", "carve", "caste", "catch",
        "cater", "catty", "caulk", "cause", "cavil", "cease", "cedar", "cello", "chafe", "chaff",
        "chain", "chair", "chalk", "champ", "chant", "chaos", "chard", "charm", "chart", "chase",
        "chasm", "cheap", "cheat", "check", "cheek", "cheer", "chess", "chest", "chick", "chide",
        "chief", "child", "chili", "chill", "chime", "china", "chirp", "chock", "choir", "choke",
        "chord", "chore", "chose", "chuck", "chump", "chunk", "churn", "chute", "cider", "cigar",
        "cinch", "circa", "civic", "civil", "clack", "claim", "clamp", "clang", "clank", "clash",
        "clasp", "class", "clean", "clear", "cleat", "cleft", "clerk", "click", "cliff", "climb",
        "cling", "clink", "cloak", "clock", "clone", "close", "cloth", "cloud", "clout", "clove",
        "clown", "cluck", "clued", "clump", "clung", "coach", "coast", "cobra", "cocoa", "colon",
        "color", "comet", "comfy", "comic", "comma", "conch", "condo", "conic", "copse", "coral",
        "corer", "corny", "corps", "couch", "cough", "could", "count", "coupe", "court", "coven",
        "cover", "covet", "covey", "cower", "coyly", "crack", "craft", "cramp", "crane", "crank",
        "crash", "crass", "crate", "crave", "crawl", "craze", "crazy", "creak", "cream", "credo",
        "creed", "creek", "creep", "creme", "crest", "crewe", "cried", "crier", "crime", "crimp",
        "crisp", "croak", "crock", "crone", "crony", "crook", "cross", "crowd", "crown", "crumb",
        "crush", "crust", "crypt", "cubby", "cubic", "cumin", "curio", "curly", "curry", "curse",
        "curve", "curvy", "cutie", "cyber", "cycle", "cynic", "daddy", "daily", "dairy", "daisy",
        "dally", "dance", "dandy", "datum", "daunt", "dealt", "death", "debar", "debit", "debug",
        "debut", "decal", "decay", "decor", "decoy", "decry", "defer", "deify", "deign", "deity",
        "delay", "delta", "delve", "demon", "demur", "denim", "dense", "depot", "depth", "derby",
        "deter", "detox", "deuce", "devil", "diary", "digit", "dilly", "dimly", "diner", "dingo",
        "dingy", "diode", "dirge", "dirty", "disco", "ditch", "ditto", "ditty", "diver", "dizzy",
        "dodgy", "dogma", "doing", "dolly", "donor", "donut", "dopey", "doubt", "dough", "dowdy",
        "dowel", "downy", "dowry", "dozen", "draft", "drain", "drake", "drama", "drank", "drape",
        "drawl", "drawn", "dread", "dream", "dress", "dried", "drier", "drift", "drill", "drink",
        "drive", "droll", "drone", "drool", "droop", "dross", "drove", "drown", "druid", "drunk",
        "dryer", "dryly", "duchy", "dully", "dummy", "dumpy", "dunce", "dusky", "dusty", "dutch",
        "duvet", "dwarf", "dweeb", "dwell", "dwelt", "dying", "eager", "eagle", "early", "earth",
        "easel", "eaten", "eater", "ebony", "eclat", "edict", "edify", "eerie", "egret", "eight",
        "eject", "eking", "elate", "elbow", "elder", "elect", "elegy", "elfin", "elide", "elite",
        "elope", "elude", "email", "embed", "ember", "emcee", "empty", "enact", "endow", "enema",
        "enemy", "enjoy", "ennui", "ensue", "enter", "entry", "envoy", "epoch", "epoxy", "equal",
        "equip", "erase", "erect", "erode", "error", "erupt", "essay", "ester", "ether", "ethic",
        "ethos", "etude", "evade", "event", "every", "evict", "evoke", "exact", "exalt", "excel",
        "exert", "exile", "exist", "expel", "extol", "extra", "exult", "eying", "fable", "facet",
        "faint", "fairy", "faith", "false", "fancy", "fanny", "farce", "fatal", "fatty", "fault",
        "fauna", "favor", "feast", "fecal", "feign", "fella", "felon", "femme", "femur", "fence",
        "feral", "ferry", "fetal", "fetch", "fetid", "fetus", "fever", "fewer", "fiber", "ficus",
        "field", "fiend", "fiery", "fifth", "fifty", "fight", "filer", "filet", "filly", "filmy",
        "filth", "final", "finch", "finer", "first", "fishy", "fixer", "fizzy", "flack", "flail",
        "flair", "flake", "flaky", "flame", "flank", "flare", "flash", "flask", "fleck", "fleet",
        "flesh", "flick", "flier", "fling", "flint", "flirt", "float", "flock", "flood", "floor",
        "flora", "floss","gable", "gaffe", "gaily", "gamer", "gamma", "gamut", "gassy", "gaudy", "gauge", "gaunt",
    "habit", "hairy", "halve", "handy", "happy", "hardy", "harem", "harpy", "harry", "harsh","right",
    "icily", "icing", "ideal", "idiom", "idiot", "idler", "idyll", "igloo", "iliac", "image",
    "jaunt", "jazzy", "jelly", "jerky", "jetty", "jewel", "jiffy", "joint", "joist", "joker",
    "kappa", "karma", "kayak", "kebab", "khaki", "kinky", "kiosk", "kitty", "knack", "knave",
    "label", "labor", "laden", "ladle", "lager", "lance", "lanky", "lapel", "lapse", "large",
    "macaw", "macho", "macro", "madam", "madly", "mafia", "magic", "magma", "maize", "major",
    "nadir", "naive", "nanny", "nasal", "nasty", "natal", "naval", "navel", "needy", "neigh",
    "oaken", "obese", "occur", "ocean", "octal", "octet", "odder", "oddly", "offal", "offer",
    "paddy", "pagan", "paint", "paler", "palsy", "panel", "panic", "pansy", "papal", "paper",
    "quack", "quail", "quake", "qualm", "quark", "quart", "quash", "quasi", "queen", "queer",
    "rabbi", "rabid", "racer", "radar", "radii", "radio", "rainy", "raise", "rajah", "rally",
    "sadly", "safer", "saint", "salad", "sally", "salon", "salsa", "salty", "salve", "salvo",
    "table", "taboo", "tacit", "tacky", "taken", "tamer", "tango", "taper", "tardy", "tarry",
    "udder", "ulcer", "ultra", "umbra", "unarm", "unary", "unbar", "uncle", "under", "undid",
    "vague", "valet", "valid", "valor", "value", "vapor", "vault", "vegan", "venom", "venue",
    "wacky", "wager", "waist", "waive", "waltz", "warty", "watch", "water", "waver", "waxen",
    "xenon", "xerox", "xylem", 
    "yacht", "yahoo", "yammer", "yanks", "yearn", "yeast", "yield", "yogic", "yodel", "young",
    "zebra", "zesty", "zippy", "zonal", "zooid", "zooms", "zombi", "zoppa", "zulus", "zygot"
    ]
mediator = Mediator(words)
machine = MachinePlayer(words)
previous_machine_guess = None


@app.route("/validate_word", methods=["POST"])
def validate_word():
    data = request.json
    word = data.get("word")

    if not word:
        return jsonify({"error": "No word provided"}), 400

    is_valid = mediator.validate_guess(word)
    return jsonify({
        "word": word,
        "exists_in_list": is_valid
    })


@app.route("/machine_guess", methods=["GET"])
def machine_guess():
    global previous_machine_guess
    feedback = mediator.get_feedback(previous_machine_guess) if previous_machine_guess else None
    machine_guess = machine.make_guess(feedback=feedback, previous_guess=previous_machine_guess)
    previous_machine_guess = machine_guess

    return jsonify({"bot_guess": machine_guess})

@app.route("/word", methods=["GET"])
def word_generate():
    t_word=mediator.emit(words)
   
    return jsonify({"wordle_guess":t_word})



if __name__ == "__main__":
    app.run(debug=True)

