#!/usr/bin/env ruby
#march string start with "h" end with "n" can have any singlecharacter in between
puts ARGV[0].scan(/h.n/).join
