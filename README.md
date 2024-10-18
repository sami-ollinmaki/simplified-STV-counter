Siirtoäänivaalitavan laskuri yksinkertaisissa tilanteissa

Tämä ohjelma on kirjoitettu laskemaan automaattisesti siirtoäänivaalitavan ääniä. Se ei ole toimiva ratkaisu jokaisessa tapauksessa, vaan se on erityisesti tehty Järvenpään Lukion opiskelijakunnan vaaleja varten. Ohjelmaa voidaan käyttää muuallakin, mutta tietyt ratkaisut eivät välttämättä sovellu hyvin.

Ohjelmiston data on tarkoitus luoda Microsoft Forms kyselyllä. Sielä kysymystyyppi "Järjestys" antaa tulokset kyselyyn liittyvässä Excel taulukossa juuri siinä muodossa, kun ne halutaankin tässä ohjelmassa.
Data on tarkoitettu tuotavaksi ohjelmistoon seuraavasti:

    - Suorita kysely
    - Poimi kyselyn Excel-taulukosta haluttu sarake
    - Laita sarake uudelle välilehdelle A sarakkeeksi, jättäen otsikon pois
    - Vie kyseinen välilehti CSV tiedostona
    - Mikäli .csv tiedosto on samassa kansiossa Python ohjelman kanssa, voit syöttää sijainniksi vain tiedoston nimen. Muussa tapauksessa on suoriteltavaa syöttää koko .csv tiedoston polku

Ohjelmistossa on selkeitä puutteita, jotka on jätetty korjaamatta, sillä ne eivät vaikuta opiskelijakunnan vaaleissa. Mikäli haluat käyttää tätä ohjelmistoa johonkin muuhun, on suositeltavaa korjata nämä puutteet.
Lisäksi koodi on suhteellisen kehnoa, sillä sen on tehnyt amatööri koodari, joka halusi vain jotain toimivaa eikä kaunista. Se on pyritty kommentoimaan mahdollisimman hyvin.
