if (false)      {} else { console.log('false is falsy'); }
if (null)       {} else { console.log('null is falsy'); }
if (undefined)  {} else { console.log('underfined is falsy'); }
if (0)          {} else { console.log('0 is falsy'); }
if (NaN)        {} else { console.log('NaN is falsy'); }
if ('')         {} else { console.log('an empty string with single-quotes is falsy'); }
if ("")         {} else { console.log('an empty string with double-quotes is falsy'); }

// Everything else is truthy

if (true)       { console.log('true is truthy'); }
if ({})         { console.log('an empty object is truthy'); }
if ([])         { console.log('an empty array us truthy'); }

if ('bob')      { console.log('a non-empty string is truthy'); }