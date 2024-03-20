# post-postman

(grafiske) API-testverktøy og GDPR

---

# case

- i et produktutviklingsteam finnes det ofte personer i ulike roller 
  med en interesse for å teste API
    - utviklere, produkteiere, dedikerte testere, designere
- API-testing burde være enkelt for folk med ulik kompetanse
    - dermed ønsker jeg å ta for meg ulike grafiske verktøy

---

# hva er å teste et API?

- det er å sende HTTP-forespørsel til en tjeneste i et miljø, 
  og verifisere at vi får riktig utslag etter det
    - (lokalt, i et testmiljø, eller i produksjon)

---

# postman

- et populært grafisk verktøy for å gjøre HTTP-forespørsler
- i tillegg til REST støttes blant annet SOAP, GraphQL og WebSockets
- muligheter for å kjøre tester av samlinger

---

# postman og innlogging

- postman legger mange features bak innlogging
  - lokal versjon har ikke mulighet for å lagre forespørsler i det hele tatt
  - man kan heller ikke kjøre tester med lokal samling
- for å registrere seg trenger man å oppgi epost
  - i jobbsammenheng vil mange sikkert legge inn jobb-eposten sin

---

# hva synes datatilsynet om det?

- min tolkning av det datatilsynet sier er at jobb-eposten din er personopplysninger
  som krever behandlingsgrunnlag
- dersom man ikke har et behandlingsgrunnlag er overføringen ulovlig
- postman som et unntak til behandlingsgrunnlag?
  - datatilsynet sier at unntak *kan* brukes dersom f.eks. 
  "Den registrerte har gitt et uttrykkelig og informert samtykke"

---

# webversjonen av postman

- postman har en webversjon (som også er bak innlogging)
- denne sender kallene dine gjennom postman sine proxy-servere
  - om du mot formodning skulle sende personopplysninger i forespørslene dine, 
  til ditt eget API, er det også sannsynligvis ulovlig
- andre programmer har også webversjoner hvor proxy-servere gjør forespørselen din
  - postman sin versjon er closed source,
    noen av de andre er i det minste open source

---

# insomnia

- grafisk grensesnitt er open source
- støtter blant annet også protokoller som GraphQL, gRPC og WebSockets
- krever innlogging dersom man vil ha mer enn én lokal samling av forespørsler, 
  og deling av disse med andre
  - krever sannsynligvis behandlingsgrunnlag dersom man vil
    benytte dette i jobbsammenheng
- har git sync som betalt feature, 
  er ellers ganske dårlig på dataportabilitet utenfor applikasjonen
  - lokalt lagrede samlinger lagres i NeDB-database
  - man kan manuelt eksportere json som kan importeres igjen, 
    men det er ikke en kjempesmud opplevelse

---

# insomnium

- open source
- fork av insomnia (versjon fra mai 2023)
- har ikke noen innlogging, koblinger til skytjenester eller tracking
- usikker hvor mange features programmet har
  med tanke på dataportabilitet og automatisert testing
  - ser uheldigvis litt dårlig ut for sync utover lokal maskin,
    men det er planlagt å åpne dette opp
- kodeeieren ser ut til å være veldig glad i mulighetene for å benytte LLMs til..
  kodegenerering av api-endepunkter??? og dette er høyt prioritert
  - de om det, i guess

---

# hoppscotch

- open source
- webversjon, først og fremst, med desktopklient og kommandolinjeverktøy i alpha
- online, men støtter offlinemodus som progressive web app
- browser extension
  - extension skrur CORS-sjekk av (på hoppscotch.io),
    slik at vanlige fetch-kall kan benyttes
  - krever "Access your data for all websites" 
    for å kunne sende requests til hvorsomhelst
- deling av samlinger kan gjøres med import/export-funksjon eller i skyløsning
  - skyløsning introduserer tidligere nevnt GDPR-problematikk 
  med mindre man setter opp hoppscotch selv (self-host)
- kan skrive tester som javascript, som kjøres hver gang man sender requests

---

# bruno

- min favoritt :)
- open source
- offline, ingen koblinger til skytjenester eller tracking, ingen innlogging
- samlinger er lagret i et åpent markup-format lokalt, 
  og kan enkelt sjekkes inn i versjonskontrollsystem som git
  - f.eks. sammen med APIet man ønsker å ha en samling av testforespørsler til?
  - dataportabilitet og samarbeid kan dermed løses
    med ditt valg av versjonskontroll
  - samlinger kan leses i grafisk grensesnitt, 
    i kommandolinje, og i vscode-extension
- tester kan skrives i javascript, eller med deklarative "assertions" i grensesnitt
- eieren av bruno ser ut til å ha ganske gode meninger om hva som kreves 
  for å fortsette å tilby et godt verktøy for allmenheten

---

# andre verktøy

det fins en del andre verktøy jeg ikke har snakket om

- curl
  - krever nok flere programmer (som `jq` og andre ting)
    for å bli et ordentlig verktøy for testing
  - krever at man er 10/10 komfortabel med kommandolinjeverktøy
- httpie
  - kommandolinjeversjonen er open source, web og desktop-versjonene er ikke det
  - krever også at man er.. 7/10, kanskje? komfortabel med kommandolinjeverktøy
- python-requests (eller aiohttp, eller andre python-greier)
  - om du er dataforsker er det nok enkelt å sette opp
    en jupyter notebook med api-kall og test assertions!
  - dette gjelder også http-bibliotek i andre språk
  - det er kanskje ikke alle på teamet som ønsker å spinne opp
    en notebook for å sjekke APIene sine?
- http-klient i koderedigeringsprogram
  - vscode
  - intellij (krever ultimate)
  - det er kanskje ikke alle på teamet som ønsker å benytte slike programmer?

---

# spørsmål?

:)

presentasjonen finnes her: https://github.com/chinatsu/postpostman
