# post-postman

(grafiske) API-testverktøy og GDPR

---

# case

- i et produktutviklingsteam finnes det ofte personer i ulike roller med en interesse for å teste API
    - utviklere, produkteiere, dedikerte testere, designere
- API-testing burde være enkelt for folk med ulik kompetanse
    - dermed ønsker jeg å ta for meg ulike grafiske verktøy

---

# hva er å teste et API?

- det er å sende HTTP-forespørsel til en tjeneste i et miljø, og verifisere at vi får riktig utslag etter det
    - (lokalt, i et testmiljø, eller i produksjon)

---

# postman[1]

- et populært grafisk verktøy for å gjøre HTTP-forespørsler
- i tillegg til REST støttes blant annet SOAP, GraphQL og WebSockets
- muligheter for å kjøre tester av samlinger (https://learning.postman.com/docs/collections/running-collections/intro-to-collection-runs/)

[1]: https://www.postman.com/

---

# postman og innlogging

- postman legger mange features bak innlogging
  - lokal versjon har ikke mulighet for å lagre forespørsler i det hele tatt
  - man kan heller ikke kjøre tester med lokal samling
- for å registrere seg trenger man å oppgi epost
  - i jobbsammenheng vil mange sikkert legge inn jobb-eposten sin

---

# hva synes datatilsynet om det?

- min tolkning av det datatilsynet sier[2] er at jobb-eposten din er personopplysninger som krever behandlingsgrunnlag
- dersom man ikke har et behandlingsgrunnlag er overføringen ulovlig

- det kan hende at man i noen tilfeller kan kalle det å opprette bruker og logge inn i postman er nødvendig og at det kan være et unntak
  - datatilsynet sier at unntak *kan* brukes dersom f.eks. "Den registrerte har gitt et uttrykkelig og informert samtykke"[3]

[2]: https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/overforing-av-personopplysninger-ut-av-eos/

---

# webversjonen av postman

- postman har en webversjon (som også er bak innlogging)
- denne sender kallene dine gjennom postman sine proxy-servere
  - om du mot formodning skulle sende personopplysninger i forespørslene dine, til ditt eget API, (uten behandlingsgrunnlag) er det også sannsynligvis ulovlig
- andre programmer har også webversjoner hvor proxy-servere gjør forespørselen din
  - postman sin versjon er closed source, noen av de andre er i det minste open source

---

# insomnia[4]

- grafisk grensesnitt er open source
- støtter blant annet også protokoller som GraphQL, gRPC og WebSockets
- krever innlogging[5] dersom man vil ha mer enn én lokal samling av forespørsler, og deling av disse med andre
  - krever sannsynligvis behandlingsgrunnlag dersom man vil benytte dette i jobbsammenheng
- har git sync som betalt feature, er ellers ganske dårlig på dataportabilitet utenfor applikasjonen
  - lokalt lagrede samlinger lagres i NeDB-database
  - man kan manuelt eksportere json som kan importeres igjen, men det er ikke en kjempesmud opplevelse

[4]: https://github.com/Kong/insomnia
[5]: https://github.com/Kong/insomnia/issues/6577

---

# insomnium[6]

- open source
- fork av insomnia (versjon fra mai 2023)
- har ikke noen innlogging, koblinger til skytjenester eller tracking
- usikker hvor mange features programmet har med tanke på dataportabilitet og automatisert testing
  - ser uheldigvis litt dårlig ut for sync utover lokal maskin, men det er planlagt å åpne dette opp[7]
- kodeeieren ser ut til å være veldig glad i mulighetene for å benytte (lokale) LLMs til.. kodegenerering av api-endepunkter??? og dette er høyt prioritert[7]
  - de om det, i guess

[6]: https://github.com/ArchGPT/insomnium
[7]: https://github.com/ArchGPT/insomnium/discussions/13

---

# hoppscotch[8]

- open source
- webversjon, først og fremst, med desktopklient og kommandolinjeverktøy i alpha
- online, men støtter offlinemodus som progressive web app
- sender forespørsler gjennom proxy (som også er open source)
  - browser extension/desktopklient kreves dersom man vil sende forespørsler til private nettverk (som localhost)
  - da tror jeg ikke proxy benyttes heller
- deling av samlinger kan gjøres med import/export-funksjon eller i skyløsning
  - skyløsning introduserer tidligere nevnt GDPR-problematikk med mindre man setter opp hoppscotch selv (self-host)

[8]: https://docs.hoppscotch.io/

---

# bruno[9]

- min favoritt :)
- open source
- offline, ingen koblinger til skytjenester eller tracking, ingen innlogging
- samlinger er lagret i et åpent markup-format lokalt, og kan enkelt sjekkes inn i versjonskontrollsystem som git
  - f.eks. sammen med APIet man ønsker å ha en samling av testforespørsler til?
  - dataportabilitet og samarbeid kan dermed løses dermed med ditt valg av versjonskontroll
  - samlinger kan leses i grafisk grensesnitt, i kommandolinje, og i vscode-extension
- tester kan skrives i javascript, eller med deklarative "assertions" i grensesnitt[10]
- eieren av bruno ser ut til å ha ganske gode meninger om hva som kreves for å fortsette å tilby et godt verktøy for allmenheten[11]

[9]: https://www.usebruno.com/
[10]: https://docs.usebruno.com/testing/introduction.html
[11]: https://github.com/usebruno/bruno/discussions/269#discussioncomment-7822943

---

# andre verktøy

det fins en del andre verktøy jeg ikke har snakket om

- curl (https://curl.se/)
  - krever nok flere programmer (som `jq` og andre ting) for å bli et ordentlig verktøy for testing
  - krever at man er 10/10 komfortabel med kommandolinjeverktøy
- httpie (https://httpie.io/)
  - kommandolinjeversjonen er open source, web og desktop-versjonene er ikke det
  - krever også at man er.. 7/10, kanskje? komfortabel med kommandolinjeverktøy
- python-requests (eller aiohttp, eller andre python-greier)
  - om du er dataforsker er det nok enkelt å sette opp en jupyter notebook med api-kall og test assertions!
  - dette gjelder også http-bibliotek i andre språk
  - det er kanskje ikke alle på teamet som ønsker å spinne opp en notebook for å sjekke APIene sine?
- http-klient i koderedigeringsprogram
  - vscode (https://github.com/Huachao/vscode-restclient)
  - intellij (krever ultimate) (https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html)
  - det er kanskje ikke alle på teamet som ønsker å benytte slike programmer?

---

# spørsmål?

:)

presentasjonen finnes her: https://github.com/chinatsu/postpostman
