# coding:utf-8

import re
import urllib2

xml_data = """
<list>

<parking>
<name></name>
<total></total>
<address></address>
<geopt></geopt>
<price>20元/時</price>
</parking>

</list>
"""

 

request = urllib2.Request('http://iteamjob.appspot.com/rest/parking', xml_data)
urllib2.urlopen(request)

