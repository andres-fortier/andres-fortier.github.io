#!/usr/bin/ruby

require 'cgi'
cgi = CGI.new('html4')

cgi.out do
  cgi.html do
    cgi.body do
      cgi.h1 {'Hola'} +
      cgi.p {Time.new()}
    end
  end
end
