#!/usr/bin/bin/env ruby
#march "hbtn", "hbttn", "hbtttn", "hbttttn" not "hbn"
puts ARGV[0].scan(/hbt+n/).join
