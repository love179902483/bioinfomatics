## The version that I used in my project is `"d3": "^7.8.1`.
> To choose a proper version in `d3` is diffult.The syntax between different versions also different.
1.  `scaleLinear()`  should be used in this version.

```
d3.scaleLinear().domain([0, d3.max(data)]).range([0.500]
```

2. `const axis = d3.axisBottom()` should be used in this version, while in last version the command is `d3.svg.axis().scale(xScale)`

```
const axis = d3.axisBottom()
```

3. In D3.4x `rangeRoundBands` was moved to the new Band scale
```javascript
d3.scaleBand()
    .range([range])
    .round([round]);

// That's equivalent to:
d3.scaleBand()
    .rangeRound([range]);

```

4. [This is a basic D3 API.](https://d3-graph-gallery.com/graph/shape.html)



