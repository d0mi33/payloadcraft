<?xml version="1.0" encoding="utf-8"?>
<!-- renders the rss feed as a readable page when opened in a browser.
     mirrors the field-manual tokens; fonts resolve relative to /blog/index.xml, the feed the theme links. -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="utf-8" indent="yes"/>
  <xsl:template match="/rss/channel">
    <html lang="en">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title><xsl:value-of select="title"/> · rss feed</title>
        <style>
          @font-face { font-family: 'Fraunces'; src: url('../fonts/fraunces-var.woff2') format('woff2'); font-weight: 100 900; }
          @font-face { font-family: 'IBM Plex Mono'; src: url('../fonts/plexmono-400.woff2') format('woff2'); font-weight: 400; }
          @font-face { font-family: 'IBM Plex Mono'; src: url('../fonts/plexmono-600.woff2') format('woff2'); font-weight: 600; }
          :root { --paper:#f4f1e9; --panel:#edeade; --card:#e7e4d5; --ink:#26251f; --dim:#7d7a6d; --accent:#c2351f; --line:#dbd7c7; --line-strong:#b9b4a0; }
          @media (prefers-color-scheme: dark) { :root { --paper:#151513; --panel:#1b1b18; --card:#21211d; --ink:#d6d2c4; --dim:#85816f; --accent:#ff5238; --line:#2b2b25; --line-strong:#3e3e35; } }
          * { box-sizing: border-box; }
          body { margin: 0; background: var(--paper); color: var(--ink); font: 15px/1.75 'IBM Plex Mono', ui-monospace, monospace; }
          .wrap { max-width: 840px; margin: 0 auto; padding: 48px clamp(18px, 4vw, 40px) 80px; }
          a { color: var(--accent); text-decoration: none; }
          a:hover { text-decoration: underline; text-underline-offset: 4px; }
          .band { display: flex; justify-content: space-between; gap: 14px; border-bottom: 1px solid var(--line-strong); padding-bottom: 9px; font-size: 9.5px; letter-spacing: .16em; text-transform: uppercase; color: var(--dim); }
          .band span:last-child { color: var(--accent); }
          h1 { font-family: 'Fraunces', Georgia, serif; font-weight: 600; font-size: clamp(34px, 5vw, 52px); letter-spacing: -.02em; line-height: 1.05; margin: 26px 0 18px; }
          .note { border: 1px dashed var(--line-strong); background: var(--panel); padding: 14px 16px; font-size: 13px; }
          .note b { color: var(--ink); }
          .url { display: block; margin-top: 8px; padding: 6px 10px; background: var(--card); border: 1px solid var(--line); font-size: 12px; overflow-wrap: anywhere; user-select: all; }
          .ledger { margin-top: 34px; border: 1px solid var(--line-strong); background: var(--panel); }
          .row { display: grid; grid-template-columns: auto 1fr; gap: 20px; align-items: baseline; padding: 14px 18px; border-bottom: 1px dashed var(--line); color: var(--ink); }
          .row:last-child { border-bottom: none; }
          .row:hover { background: var(--card); text-decoration: none; }
          .row:hover .t { color: var(--accent); }
          .d { color: var(--dim); font-size: 11px; }
          .t { font-size: 14px; font-weight: 600; }
          .back { margin-top: 22px; font-size: 11.5px; letter-spacing: .12em; }
        </style>
      </head>
      <body>
        <div class="wrap">
          <div class="band"><span>DOC · RSS 2.0 FEED</span><span>MACHINE-READABLE</span></div>
          <h1><xsl:value-of select="title"/></h1>
          <div class="note">
            <b>This is an RSS feed.</b> Paste this address into a feed reader (NetNewsWire, Feedly, Inoreader, Thunderbird…) and new posts show up there automatically. No account, no email, no tracking.
            <span class="url"><xsl:value-of select="atom:link/@href" xmlns:atom="http://www.w3.org/2005/Atom"/></span>
          </div>
          <div class="ledger">
            <xsl:for-each select="item">
              <a class="row">
                <xsl:attribute name="href"><xsl:value-of select="link"/></xsl:attribute>
                <span class="d"><xsl:value-of select="substring(pubDate, 6, 11)"/></span>
                <span class="t"><xsl:value-of select="title"/></span>
              </a>
            </xsl:for-each>
          </div>
          <p class="back"><a><xsl:attribute name="href"><xsl:value-of select="link"/></xsl:attribute>◂◂ back to the site</a></p>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
