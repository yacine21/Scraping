import io
import sys
from lxml import etree

xml_filename = sys.argv[1]
dtd_filename = sys.argv[2]

with io.open(xml_filename, 'r', encoding="ISO-8859-1") as xml_file, io.open(dtd_filename, 'r', encoding="UTF-8") as dtd_file:
    try:
        document = etree.parse(xml_file, parser=etree.XMLParser(remove_blank_text=True))
        dtd = etree.DTD(dtd_file)
        dtd.assertValid(document)
        print("OK")
    except IOError:
        print('IO Error')
    except etree.DocumentInvalid as err:
        print(str(err.error_log))
    except etree.XMLSyntaxError as err:
        print(str(err.error_log))
    except object as err:
        print(str(err.error_log))


