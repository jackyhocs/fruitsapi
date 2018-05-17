from voluptuous import Schema, All, Optional, Required, Coerce

post_schema = Schema({
    Required("name"): All(str, msg="Invalid fruit name entered"),
    Required('sweetness'): All(Coerce(int), msg="Invalid sweetness entered"),
    Optional('country'): All(str, msg="Invalid city entered")
})
