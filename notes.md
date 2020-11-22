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
