import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const rarity = [
    "Common",
    "Rare",
    "Team of the Week",
    "Icon",
    "Winter Wildcards",
    "UT Heroes",
    "NumeroFUT",
    "Total Rush",
    "Trailblazers",
    "SQUAD FOUNDATIONS",
    "Thunderstruck",
    "Globetrotters",
    "Centurions",
    "Ultimate Succession",
    "UCL Road to the Knockouts",
    "Track Stars",
    "FC Pro Live",
    "Team of the Year",
    "Winter Wildcards Icon",
    "Winter Wildcards Hero",
    "Ballon d'Or",
    "TOTY Honourable Mentions",
    "Thunderstruck ICON",
    "World Tour",
    "Champions Mastery",
    "Squad Battles Mastery",
    "Rivals Mastery",
    "Flashback Player",
    "Prime Hero",
    "TOTY Icon",
    "Centurions Icon",
    "Track Stars Hero",
    "UEL Road to the Knockouts",
    "Ultimate Succession Icon",
    "Winter Champions",
    "Showdown Plus",
    "UWCL Road to the Knockouts",
    "End Of An Era",
    "On This Day Icon",
    "POTM SERIE A",
    "POTM Premier League",
    "Liga F POTM",
    "Moments",
    "POTM LALIGA EA SPORTS",
    "POTM Ligue 1",
    "POTM Bundesliga",
    "Ultimate Succession Hero",
    "Mode Mastery",
    "UECL Road to the Knockouts",
    "SHOWDOWN",
    "Ultimate Cover Star",
    "On This Day Hero",
    "TOTY Eras 2002 ICON",
    "TOTY Evolution",
    "Winter Wildcards Evolution",
    "Centurions Evolution",
    "Bundesliga POTM",
    "Purple Evo",
    "Dynamic Duos",
    "UCL Road to the Final",
    "Legendary",
    "Standard",
    "POTM EREDIVISIE",
    "Ultimate",
    "Premium",
    "Vintage",
    "Epic",
    "Select",
    "Squad Building Challenge",
    "Ones to Watch",
    "Ultimate Team Champions",
    "Ultimate Team Champions Pro",
    "Pro Player",
    "Domestic Man of the Match",
    "Evolutions III",
    "Evolutions II",
    "Evolutions I",
    "In-Progress Evolution",
    "Origin Hero"
  ];

  const position = [
    "GK", "RB", "CB", "LB", "CDM", "RM", "CM", "LM", "CF", "RW", "ST", "LW"
  ];
  
  const chemistryStyle = [
    "Sniper",
    "Finisher",
    "Deadeye",
    "Marksman",
    "Hawk",
    "Artist",
    "Architect",
    "Powerhouse",
    "Maestro",
    "Engine",
    "Sentinel",
    "Guardian",
    "Gladiator",
    "Backbone",
    "Anchor",
    "Hunter",
    "Catalyst",
    "Shadow",
    "Wall",
    "Shield",
    "Cat",
    "Glove",
    "GK Basic"
  ];

  const countries = [
    "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", 
    "Anguilla", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", 
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", 
    "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", 
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
    "British Virgin Islands", "Brunei Darussalam", "Bulgaria", "Burkina Faso", 
    "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde Islands", 
    "Cayman Islands", "Central African Republic", "Chad", "Chile", "China PR", 
    "Chinese Taipei", "Colombia", "Comoros", "Congo", "Congo DR", "Cook Islands", 
    "Costa Rica", "Croatia", "Cuba", "Curaçao", "Cyprus", "Czechia", 
    "Côte d'Ivoire", "Denmark", "Djibouti", "Dominica", "Dominican Republic", 
    "Ecuador", "Egypt", "El Salvador", "England", "Equatorial Guinea", 
    "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Faroe Islands", "Fiji", 
    "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", 
    "Gibraltar", "Greece", "Greenland", "Grenada", "Guam", "Guatemala", 
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong", 
    "Hungary", "Iceland", "India", "Indonesia", "International", "Iran", 
    "Iraq", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", 
    "Kenya", "Korea DPR", "Korea Republic", "Kosovo", "Kuwait", "Kyrgyzstan", 
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", 
    "Lithuania", "Luxembourg", "Macau", "Madagascar", "Malawi", "Malaysia", 
    "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", 
    "Moldova", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", 
    "Myanmar", "Namibia", "Nepal", "Netherlands", "New Caledonia", 
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", 
    "Northern Ireland", "Norway", "Oman", "Pakistan", "Palestine", "Panama", 
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", 
    "Puerto Rico", "Qatar", "Republic of Ireland", "Romania", "Russia", 
    "Rwanda", "Samoa", "San Marino", "Saudi Arabia", "Scotland", "Senegal", 
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", 
    "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", 
    "Spain", "Sri Lanka", "St. Kitts and Nevis", "St. Lucia", 
    "St. Vincent and the Grenadines", "Sudan", "Suriname", "Sweden", 
    "Switzerland", "Syria", "São Tomé e Príncipe", "Tahiti", "Tajikistan", 
    "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", 
    "Trinidad and Tobago", "Tunisia", "Turkmenistan", "Turks and Caicos Islands", 
    "Türkiye", "US Virgin Islands", "Uganda", "Ukraine", "United Arab Emirates", 
    "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", 
    "Vietnam", "Wales", "Yemen", "Zambia", "Zimbabwe"
  ];

  const [filters, setFilters] = useState({
    rarity: '',
    position: '',
    chemistryStyle: '',
    country: '',
    maxPrice: '',
    verificationCode: ''
  });

  const handleSearch = () => {
    console.log('Filters:', filters);
    fetch('/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(filters)
  })
  .then(response => response.json())
  .then(data => console.log("Data received:", data))
  .catch(error => console.error("Error:", error));
  
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilters((prevFilters) => ({
      ...prevFilters,
      [name]: value
    }));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1><em>EAFCMarketBot</em></h1>
      </header>
      <div className="filter-container">
        <select name="rarity" className="filter-dropdown" onChange={handleChange}>
          <option value="">Rarity</option>
          {rarity.map((item, index) => (
            <option key={index} value={item}>{item}</option>
          ))}
        </select>
        <select name="position" className="filter-dropdown" onChange={handleChange}>
          <option value="">Position</option>
          {position.map((pos, index) => (
            <option key={index} value={pos}>{pos}</option>
          ))}
        </select>
        <select name="chemistryStyle" className="filter-dropdown" onChange={handleChange}>
          <option value="">Chemistry Style</option>
          {chemistryStyle.map((style, index) => (
            <option key={index} value={style}>{style}</option>
          ))}
        </select>
        <select name="country" className="filter-dropdown" onChange={handleChange}>
          <option value="">Country</option>
          {countries.map((country, index) => (
            <option key={index} value={country}>{country}</option>
          ))}
        </select>
        <input
          type="number"
          name="maxPrice"
          className="filter-input"
          placeholder="Max Price"
          min="0"
          max="10000000"
          onChange={handleChange}
        />
        <input
          type="number"
          name="verificationCode"
          className="filter-input"
          placeholder="Verification Code"
          min="100000"
          max="999999"
          onChange={handleChange}
        />
        <button onClick={handleSearch} className="filter-button">Search</button>
      </div>
    </div>
  );
}

export default App;
