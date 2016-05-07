---
layout: default
title: Laboratorio 4 - UTN - SMA
---

# Laboratorio 4

## Clases
* Clase 1
  * [Transparencias](material/Clase01.pdf)
* Clase 2
  * [Transparencias](material/Clase02.pdf)
* Clase 3
  * [Archivos grep](material/Clase03Comando.tar.gz)
  * [Transparencias](material/Clase03.pdf)
* Clase 4
  * [Transparencias](material/Clase04.pdf)
* Clase 5
  * [Transparencias](material/Clase05.pdf)
* Clase 6
  * [Transparencias](material/Clase06.pdf)
* Clase 7
  * [Transparencias](material/Clase07.pdf)
* Clase 8
  * [Transparencias](material/Clase08.pdf)
* Clase 9
  * [CGI Python - hello.py](material/hello.py)
  * [CGI Ruby - otro.rb](material/otro.rb)
  * [Transparencias](material/Clase09.pdf)
* Clase 10
  * [Transparencias](material/Clase10.pdf)
* Clase 11
  * [Transparencias](material/Clase11.pdf)
* Clase 12
  * [Transparencias](material/Clase12.pdf)
* Clase 13
  * [Transparencias](material/Clase13.pdf)
* Clase 14
  * [Transparencias](material/Clase14.pdf)
* Clase 15
  * [Transparencias](material/Clase15.pdf)

Primer seed

```ruby
joeUser = User.new(
  :email                 => "joe@example.com",
  :password              => "12345678",
  :password_confirmation => "12345678"
)
joeUser.save!

janeUser = User.new(
  :email                 => "jane@example.com",
  :password              => "12345678",
  :password_confirmation => "12345678"
)
janeUser.save!
```

Segundo seed

```ruby
Article.create!(title: 'First Post',  text: 'My first post!', author: joeUser);
Article.create!(title: 'Second Post', text: 'Another post',   author: joeUser);
Article.create!(title: 'Third Post',  text: 'Yet another',    author: janeUser);
```


