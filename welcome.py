"""
A new default start page for the DiPP Instance
$Id
"""
DEFAULT_PAGE = "welcome-to-dipp"
WELCOME_TITLE = "Willkommen zu Ihrem individuellen Testzugang zu DiPP"
WELCOME_DESCRIPTION = """
Mit diesem Testzugang können Sie die Funktionen des Publikationssystems kennenlernen. Es ist Ihre persönliche Spielwiese. Sie können also frei schalten und walten.
"""
WELCOME_TEXT = """
<p>
    Das Erstellen und Editieren von Dokumenten ist nur möglich, 
    wenn Sie  angemeldet sind (s. Funktion &quot;login&quot; in der Kopfzeile).
    Sollten sie keine  persönlichen Zugangsdaten erhalten haben, wenden Sie sich
    bitte an  dipp-tech[a]hbz-nrw.de. Nach der Anmeldung erscheinen 
    zusätzliche Menüleisten  (eine blaue und eine grüne), die Ihnen die 
    Erstellung und Bearbeitung von  Dokumenten erlauben. Sie benötigen 
    anfänglich nur die grünen Menüleisten --  im Folgenden &quot;Reiter&quot; genannt. 
    Nachdem Sie sich abgemeldet haben,  verschwinden die Menüleisten wieder 
    (Endansicht der WWW-Seite, wie sie Ihre  zukünftigen Leser sähen).
</p>

<h2>Editieren von bereits bestehenden Dokumenten</h2>

<ol>
    <li><em>Anmelden:</em> In der Kopfzeile befindet sich ein Link zur <a href="/chemnitzdemo/login_form">Login-Seite</a>.</li>
    <li>    <em>Bearbeiten:</em> Wählen Sie den Reiter &quot;Bearbeiten&quot;. In den Textboxen    kann der Kurzname (Teil der URL), die Beschreibung (der fett-formatierte    Text unter der Überschrift, nicht obligatorisch) und der Haupttext    bearbeitet werden.<br />
    Es gibt drei Optionen, den Haupttext zu bearbeiten:<br />
    <dl>     <dt>Textboxen:</dt>      <dd>Der Text wird in Textboxen einen normalen Webformulars editiert. Das     ist der Standard und funktioniert mit allen Browsern</dd>      <dt>FCKEditor:</dt>      <dd>FCKEditor ist ein <abbr title="What you see is what you get">WYSYWIG</abbr>-Editor, der ähnliche     Funktionalitäten wie eine normale Textverabeitung zur Verfügung stellt. Um FCKEditor zu benutzen, wird ein aktueller Browser benötigt. FCKEditor ist bereits     voreingestellt.<br />
    </dd>      <dt>Externer Editor:</dt>      <dd>Um einen Editor Ihrer Wahl zu benutzen, muß auf Ihrem PC zusätzlich     das Program <a href="http://plope.com/software/ExternalEditor">zopeedit</a> installiert     werden. Beim Klick auf das Bleistiftsymbol wird dann das Dokument     heruntergeladen, mit einem Editor Ihrer Wahl geöffnet und beim Speichern     automatisch wieder auf den Server hochgeladen. Diese Option richtet sich     an fortgeschrittene Benutzer.<br />
    </dd>    </dl>   </li>
    <li><em>Speichern:</em> Ein Klick auf den <code>Speichern</code>-Button   speichert die Seite. Sie sehen dann eine Endansicht des einzelnen Dokuments.   (Für die Endansicht des ganzen WWW-Auftritts müssen sie sich, wie bereits   erwähnt, abmelden.)</li>
</ol>

<h2>Erstellen von neuen Dokumenten</h2>

<ol>
    <li>    <em>Auswählen:</em> Unterhalb der grünen Reiter befindet sich ein Auswahlmenu    &quot;Neuen Artikel hinzufügen&quot;. Der gewählte Artikeltyp wird angelegt und eine    entsprechende Eingabemaske öffnet sich.<br />
    <br />
    Die am häufigsten benötigten Typen:     <dl>     <dt>Dokument</dt>      <dd>Textdokumente</dd>      <dt>Ordner</dt>      <dd>Ordner dienen der Organisation von Artikeln und erscheinen nach der     Veröffentlichung (s.u.) in der linken Navigation</dd>      <dt>Bild</dt>      <dd>Bilddateien (jpg, gif, png)</dd>      <dt>Nachricht</dt>      <dd>Es wird automatisch eine Übersichtsseite erstellt (Link in der oberen     Navigationsleiste)</dd>    </dl>   </li>
</ol>
<h2>Veröffentlichen</h2>
<p>Um einen Artikel oder ein anderes Objekt zu veröffentlichen, damit es auch  andere außer Ihnen sehen können, muß der Status auf 'Veröffentlichen' gesetzt  werden. Dazu dient das Dropdown-Menu ganz rechts unterhalb der grünen  Reiter.<br />
</p>
<p><strong>Publikationen<br />
</strong>Für die eigentlichen Publikationen (z.B.  begutachtete Artikel) steht eine ausgefeiltere Form der Veröffentlichung zur  Verfügung, die in der <a href="http://www.dipp.nrw.de/download/userdoc.pdf">Benutzeranleitung</a>  beschrieben wird.<br />
</p>
"""
