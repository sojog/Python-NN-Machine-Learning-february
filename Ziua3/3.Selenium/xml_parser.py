from lxml import etree

# Citim și parsăm direct fișierul XML
tree = etree.parse("fisier2.xml")
root = tree.getroot()

# Găsește toate deployment-urile folosind XPath
deployments = root.xpath("//deployment/@name")

# Afișează rezultatele
for deployment in deployments:
    print(deployment)