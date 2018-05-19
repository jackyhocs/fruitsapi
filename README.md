# fruitsapi

Example entry from database
```
{
  'id': (UUID4),
  'name': (string),
  'sweetness': (int),
  'country': (string)
}
```

## GET
Retrieves a specific entity

0.0.0.0:80/fruits/\<uuid4\>

## PUT
Updates a specific entity

0.0.0.0:80/fruits/\<uuid4\>

with payload
```
{
  'sweetness': -500
}
```

will modify the existing fruit's sweetness to -500

## DELETE
Deletes a specific entity

0.0.0.0:80/fruits/\<uuid4\>

## POST
Creates an entity

0.0.0.0:80/fruits/

with payload
```
{
  'name': (string),
  'sweetness': (int),
  'country': (string)
}
```
the id will be a randomly generated UUID

## GET
Retrieves entities that match the provided params

0.0.0.0:80/fruits/?sweetness=\<int\>&country=\<string\>
