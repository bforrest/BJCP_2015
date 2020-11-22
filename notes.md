pulling xml data isn't the hard part, it is matching all of the whacky tags that have

````xml
 <w:r w:rsidRPr="00FF4E4A">
        <w:rPr>
          <w:rFonts w:ascii="Garamond" w:hAnsi="Garamond"/>
          <w:i/>
          <w:sz w:val="20"/>
          <w:szCs w:val="20"/>
        </w:rPr>
        <w:t>The BJCP grants the right to make copies for use in</w:t>
      </w:r>
      <w:r w:rsidRPr="00FF4E4A">
        <w:rPr>
          <w:rFonts w:ascii="Garamond" w:hAnsi="Garamond"/>
          <w:i/>
          <w:sz w:val="20"/>
          <w:szCs w:val="20"/>
        </w:rPr>
        <w:br/>
        <w:t xml:space="preserve"> BJCP-sanctioned competitions or for educational/judge training purposes. </w:t>
      </w:r>
    ```

Look behind has to be fixed-width in python

```python
(?<=\[)(.*?)(?=\])
````

(?:<w:t>)(.\*?)(?=<\/w:t>)

This one looks promising hte regexr.com

```javascript
(?<=(<w:t>)|(w:t xml:space="preserve">))(.*?)(?=<\/w:t>)
```

- 2:00 After looking at the variety of exports formats from the style guide work doc, I stumbled upon the "dev.bjcp.org/styles" portion of the website. This has structured, delimited files that I'm going to try and screen screen to compse the dataset for my flassh cards.

I something related for National Homebrew Contest entry data using Python and beautiful soup.

The strucutre looks like this:

```html
<div class="blog patinated home-loop">
<article>
  <h1 class="entry-header">## <a href="">Category Name</a>
  <div class="entry-content about-beer-style">
  <p>Notes about category</p>
</article>
<article>
  <h1 class="entry-title">
    ##A <a href=""> Style Name</a>
  </h1>
  <div class="entry-content about-beer-style clearfix">
    <p>This style is ...</p>
    <div class="overall-impression"><h2>Overall Impression</h2><p>Based on declared clone beer.</p>
  </div>
    <div class="aroma"><h2>Aroma / Appearance / Flavor / Mouthfeel</h2><p></p><p>Based on declared clone beer.</p>
      <p></p>
    </div>
  <div class="comments"><h2>Comments</h2><p>Intended as a catch-all location for specific beers that are based on unique commercial examples that don’t fit existing styles.</p>
  </div>
  <div class="entry-instructions"><h2>Entry Instructions</h2><p>The entrant must specify the name of the commercial beer being cloned, specifications (vital statistics) for the beer, and either a brief sensory description or a list of ingredients used in making the beer. Without this information, judges who are unfamiliar with the beer will have no basis for comparison.</p>
  </div>
   <div class="vital-statistics"><h2>Vital Statistics</h2>
    <div class="table">
        <div class="row">
            <div class="cell">
              <h3>IBU</h3></div><div class="cell"><p>60 - 120</p></div></div>
              <div class="row"><div class="cell"><h3>SRM</h3></div><div class="cell"><p>6 - 14</p></div></div>
              <div class="row"><div class="cell"><h3>OG</h3></div><div class="cell"><p>1.065 - 1.085</p></div></div>
              <div class="row"><div class="cell"><h3>FG</h3></div><div class="cell"><p>1.008 - 1.018</p></div></div>
              <div class="row"><div class="cell"><h3>ABV</h3></div><div class="cell"><p>7.5% - 10%</p></div></div>
            </div>
        </div>
    </div>
    <div class="style-attributes"><h2>Style Attributes</h2><p><svg class="svg-inline--fa fa-tags fa-w-20" aria-hidden="true" focusable="false" data-prefix="fa" data-icon="tags" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512" data-fa-i2svg=""><path fill="currentColor" d="M497.941 225.941L286.059 14.059A48 48 0 0 0 252.118 0H48C21.49 0 0 21.49 0 48v204.118a48 48 0 0 0 14.059 33.941l211.882 211.882c18.744 18.745 49.136 18.746 67.882 0l204.118-204.118c18.745-18.745 18.745-49.137 0-67.882zM112 160c-26.51 0-48-21.49-48-48s21.49-48 48-48 48 21.49 48 48-21.49 48-48 48zm513.941 133.823L421.823 497.941c-18.745 18.745-49.137 18.745-67.882 0l-.36-.36L527.64 323.522c16.999-16.999 26.36-39.6 26.36-63.64s-9.362-46.641-26.36-63.64L331.397 0h48.721a48 48 0 0 1 33.941 14.059l211.882 211.882c18.745 18.745 18.745 49.137 0 67.882z"></path></svg><!-- <i class="fa fa-tags"></i> -->  <a href="https://dev.bjcp.org/style-tags/bitter/" rel="tag">bitter</a>, <a href="https://dev.bjcp.org/style-tags/craft-style/" rel="tag">craft-style</a>, <a href="https://dev.bjcp.org/style-tags/hoppy/" rel="tag">hoppy</a>, <a href="https://dev.bjcp.org/style-tags/ipa-family/" rel="tag">ipa-family</a>, <a href="https://dev.bjcp.org/style-tags/north-america/" rel="tag">north-america</a>, <a href="https://dev.bjcp.org/style-tags/pale-color/" rel="tag">pale-color</a>, <a href="https://dev.bjcp.org/style-tags/top-fermented/" rel="tag">top-fermented</a>, <a href="https://dev.bjcp.org/style-tags/very-high-strength/" rel="tag">very-high-strength</a> </p></div>
</article>
<article>
</article>
</div>
```
