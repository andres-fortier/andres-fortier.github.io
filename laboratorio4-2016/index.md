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
* Clase 23
  * [Transparencias](material/Clase23.pdf)

```ruby
<%= f.fields_for :profile do |ff| %>
 <div class="form-group">
  <%= ff.label :first_name %>
  <%= ff.text_field :first_name, class: 'form-control' %>
 </div>
 <div class="form-group">
  <%= ff.label :last_name %>
  <%= ff.text_field :last_name, class: 'form-control' %>
 </div>
 <div class="form-group">
  <%= ff.label :date_of_birth %>
  <%= ff.date_field :date_of_birth, class: 'form-control' %>
 </div>
<% end %>
```

```ruby
class RegistrationsController < Devise::RegistrationsController

  private

  def account_update_params
    params
     .require(:user)
     .permit(:email, :password, :password_confirmation, 
       :current_password,
       profile_attributes: [
         :id, 
         :first_name, 
         :last_name, 
         :date_of_birth
     ])
  end
end
```

```ruby
<% if user_signed_in? %>
  <li> <p class="navbar-text"> Logged in as
    <% if current_user.profile.first_name.present? %>
      <%= current_user.profile.first_name %>
    <% else %>
      <%= current_user.email %>
    <% end %>
  </p> <li>
  <%= link_to('Logout', destroy_user_session_path, :method => :delete) %>
  </li>
<% else %>
```

```ruby
class ProfilesController < ApplicationController
  after_action :verify_authorized

  def edit
    @profile = current_user.profile
    authorize @profile
  end

  def update
    @profile = current_user.profile
    authorize @profile
    @profile.update!(profile_params)
    flash[:notice] = "Your profile has been updated."
    render 'edit'
  end

 private

  def profile_params
    params.require(:profile).permit(:first_name, :last_name, :date_of_birth)
  end
end
```

```ruby
<%= form_for @profile do |f| %>
 <div class="form-group">
  <%= f.label :first_name %>
  <%= f.text_field :first_name, class: 'form-control' %>
 </div>
 <div class="form-group">
  <%= f.label :last_name %>
  <%= f.text_field :last_name, class: 'form-control' %>
 </div>
 <div class="form-group">
  <%= f.label :date_of_birth %>
  <%= f.date_field :date_of_birth, class: 'form-control' %>
 </div>
  <p>
    <%= f.submit 'Update', :class => 'btn btn-primary' %>
  </p>
<% end %>
```

* Clase 24

```ruby
if @profile.phones.empty?
  @profile.phones << Phone.new(
    phone_type: 'Mobile', 
    number: '(011) 154789345634')
end
```

```html
  <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Phones</h3>
    </div>
    <div class="panel-body">
      <%= f.fields_for :phones do | form_builder | %>
        <%= render "phone_fields", :f => form_builder %>
      <% end %>
    </div>
  </div>
```

```html
<div class="form-inline">
   <div class="form-group">
    <%= f.label :phone_type %>
    <%= f.select(:phone_type,
       ['Mobile', 'Work', 'Home'], 
       {}, 
       {:class => 'form-control'}) %>
  </div>
  <div class="form-group">
    <%= f.label :number %>
    <%= f.text_field :number, class: 'form-control' %>
  </div>
</div>
```

```html
  <div class="form-group">
    <%= f.check_box :_destroy %>
    <%= f.label :_destroy, "Remove" %>
  </div>
```

```html
  <div class="form-group">
    <%= f.hidden_field :_destroy %>
    <a href="#" onclick="removePhone(this)">Remove</a>
  </div>
```

```html
function removePhone(linkNode) {
  var link = $(linkNode);
  var myFormGroup = link.parent();
  console.log(myFormGroup.find("input[type=hidden]"));
}
```

```ruby
    if @profile.phones.empty?
      @profile.phones << Phone.new(phone_type: 'Mobile', number: '11')
      @profile.phones << Phone.new(phone_type: 'Mobile', number: '22')
      @profile.phones << Phone.new(phone_type: 'Mobile', number: '33')
    end
```

```ruby
<%
 new_phone = Phone.new
 fields = f.fields_for(:phones, new_phone) do |fb|
  render("phone_fields", :f => fb)
 end
 js = escape_javascript(fields)
 fn = html_escape("addPhone($('#phones'), \"#{js}\")")
 concat(raw("<a href=\"#\" onclick=\"#{fn}\">Add</a>"))
%>
```

```ruby
<%
 new_phone = Phone.new
 fields = f.fields_for(:phones, 
	new_phone, 
	:child_index => "id_placeholder") do |fb|
  render("phone_fields", :f => fb)
 end
 js = escape_javascript(fields)
 fn = html_escape("addPhone($('#phones'), \"#{js}\")")
 concat(raw("<a href=\"#\" onclick=\"#{fn}\">Add</a>"))
%>
```

```javascript
function addPhone($parent, formHTML) {
  var new_id = new Date().getTime();
  var regexp = new RegExp("id_placeholder", "g");
  var content = formHTML.replace(regexp, new_id)
  $parent.append(content);
}
```

```html
  <div class="form-group">
    <%= f.hidden_field :_destroy %>
    <a href="#" class="btn btn-warning" onclick="removePhone(this)">
      <span class="glyphicon glyphicon-minus"></span>
    </a>
  </div>
```

```ruby
<%
 new_phone = Phone.new
 fields = f.fields_for(:phones, 
	new_phone, 
	:child_index => "id_placeholder") do |fb|
  render("phone_fields", :f => fb)
 end
 js = escape_javascript(fields)
 fn = html_escape("addPhone($('#phones'), \"#{js}\")")
      concat(raw("<a href=\"#\" class=\"btn btn-primary\" onclick=\"#{fn}\"><span class=\"glyphicon glyphicon-plus\"></span></a>"))
%>
```

