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
* Clase 16
  * [Transparencias](material/Clase16.pdf)
* Clase 17
  * [Transparencias](material/Clase17.pdf)
* Clase 18
  * [Transparencias](material/Clase18.pdf)

```ruby
<% @article.categories.each do |category| %>
  <span class="label label-primary">
    <%= category.name %>
  </span>
<% end %>
```
* Clase 19
  * [Transparencias](material/Clase19.pdf)

* Clase 20
  * [Transparencias](material/Clase20.pdf)

```ruby
require "rails_helper"

RSpec.describe ArticlePolicy, :type => :model do
  subject { ArticlePolicy }

  permissions :new? do
    it "is denied to non-logged users" do
      expect(subject).not_to permit(nil, Article)
    end

    it "is allowed to any logged in user" do
      expect(subject).to permit(User.new, Article)
    end
  end
end
```

```ruby
require "rails_helper"

RSpec.describe ArticlePolicy, :type => :model do
  subject { ArticlePolicy }

  let(:user)   {User.new(email: "user@example.com", password: "12345678", password_confirmation: "12345678")}
  let(:author) {User.new(email: "author@example.com", password: "12345678", password_confirmation: "12345678")}
  let(:admin) do
    user = User.new(email: "admin@example.com", password: "12345678", password_confirmation: "12345678")
    user.add_role :admin
    user
  end

  let(:article) {Article.new(title: "The title", text: "The body", author: author)}

  permissions :new? do
    it "is denied to non-logged users" do
      expect(subject).not_to permit(nil, Article)
    end

    it "is allowed to any logged in user" do
      expect(subject).to permit(user, Article)
    end
  end

  permissions :destroy? do
    it "is denied to non-logged users" do
      expect(subject).not_to permit(nil, article)
    end

    it "is denied if the user is not the author" do
      expect(subject).not_to permit(user, article)
    end

    it "is allowed if the user is the article author" do
      expect(subject).to permit(author, article)
    end

    it "is allowed if the user is an admin" do
      expect(subject).to permit(admin, article)
    end
  end
end
```

```ruby
require "rails_helper"

RSpec.describe User, :type => :model do

  let(:user)    {User.create!(email: "user@example.com", password: "12345678", password_confirmation: "12345678")}
  let(:author)  {User.create!(email: "author@example.com", password: "12345678", password_confirmation: "12345678")}
  let(:article) {Article.create!(title: "The title", text: "The body", author: author)}
  let(:test_category_name) {"Test Category"}

  describe "::titles_in_category" do

    it "return an empty array if the user has no associated articles" do
      expect(user.titles_in_category(test_category_name)).to be_empty
    end

    it "returns an empty array if the user has an article with no categories" do
      expect(author.titles_in_category(test_category_name)).to be_empty
    end

    it "returns an empty array if the user has a categorized article but the categories do not match" do
      new_category = Category.create!(name: "New category")
      article.categories << new_category
      expect(author.titles_in_category(test_category_name)).to be_empty
    end

    it "returns the article title if the user has an article with the requested category name" do
      new_category=Category.create!(name: test_category_name)
      article.categories << new_category
      expect(author.titles_in_category(test_category_name)).to eq([article.title])
    end
  end
end
```

```ruby
require "rails_helper"

RSpec.describe Article, :type => :model do

  let(:author) {User.new(email: "author@example.com", password: "12345678", password_confirmation: "12345678")}

  describe "Validations" do

    it "is not valid if title is absent" do
      expect(Article.new(author: author)).not_to be_valid
    end

    it "is not valid if the title's length is less than 5 characters" do
      expect(Article.new(author: author, title: "Test")).not_to be_valid
    end

    it "is valid if the title's length is 5 characters or more" do
      expect(Article.new(author: author, title: "Tests")).to be_valid
      expect(Article.new(author: author, title: "Test #2")).to be_valid
    end
  end
end
```

```ruby
require "rails_helper"

RSpec.describe ArticlesController, :type => :controller do

  let(:user) {
    User.create!(email: "author@example.com", password: "12345678", password_confirmation: "12345678")
  }

  before(:each) do
    sign_in user
  end

  describe 'GET index' do

    it "returns 200 (ok) response code" do
      get :index
      expect(response).to have_http_status(:ok)
    end

    it "renders the index template" do
      get :index
      expect(response).to render_template("index")
    end

    it "leaves an empty relationship on @articles if there are no articles" do
      get :index
      expect(assigns(:articles)).to be_empty
    end

    it "assigns the latest 10 posts to @articles" do
      Article.create!(title: "Post number 1", text: "My first post!", author: user)
      last_articles = (2..11).map do |i|
        Article.create!(title: "Post number #{i}", text: "My #{i} post!", author: user)
      end
  
     get :index
     expect(assigns(:articles)).to eq(last_articles.reverse)
   end
  end
end
```
* Clase 21
  * [Transparencias](material/Clase21.pdf)
* Clase 22
  * [Transparencias](material/Clase22.pdf)
