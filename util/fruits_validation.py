from voluptuous import Schema, All, Optional, Required, Coerce, Any

post_schema = Schema({
    Required("name"): All(str, msg="Invalid fruit name entered"),
    Required('sweetness'): All(Coerce(int), msg="Invalid sweetness entered"),
    Optional('country'): Any(None, All(str, msg="Invalid city entered"))
})

put_schema = Schema({
    Optional("name"): Any(None, All(str, msg="Invalid fruit name entered")),
    Optional('sweetness'): Any(None, All(Coerce(int), msg="Invalid sweetness entered")),
    Optional('country'): Any(None, All(str, msg="Invalid city entered"))
})

get_schema = Schema({
    Optional('country'): Any(None, All(str, msg="Invalid city entered")),
    Optional('sweetness'): Any(None, All(Coerce(int), msg="Invalid sweetness entered"))
})
