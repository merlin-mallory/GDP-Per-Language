import React from "react"

const Methodology = () => {
    return(
        <div className="Methodology">
            <h1>Methodology</h1>
            <h3>How the data sources and measures were decided:</h3>

            <p>This project’s data is scraped from the World Bank and IMF. This project will examine both nominal GDP (in
            current US dollars) and GDP PPP (in current international dollars). In general, the nominal GDP measure is
            better for comparing similar developed entities, and the GDP PPP measure is better for comparing dissimilar
            developed entities. However it is important to keep in mind that many languages will contain collections of both
            developed and developing countries. However, in general, the nominal GDP measure will tend to favor languages
            that mostly contain developed countries with strong formal sectors, while the GDP PPP measure will provide a
            more balanced view of developing countries with strong informal sectors.</p>

            <p>If you’re interested in learning more about GDP PPP, then please check out this link: <a href="https://simple.wikipedia.org/wiki/Purchasing_power_parity">https://simple.wikipedia.org/wiki/Purchasing_power_parity</a></p>

            <h3>How the default country-to-language relationships were generated:</h3>

        There are several ways to approximate the economic value of a language. This project analyzes the language
        demographics of each country on Wikipedia. If the country’s language demographics cannot be found on Wikipedia,
        then that country’s GDP will be assigned to the “Other” language group.

        However, if the country’s language demographics can be found, and if greater than 50% of a country's native
        population are L1 (native) speakers of a single language, then that country’s entire GDP is assigned to the
        largest language. If no single language reaches the 50% mark for inclusion, then that country's entire GDP is
        assigned to the "Other" category. This does not account for the impact of L2 speakers.

        I grouped all dialects together, even though some are mutually unintelligible. This is especially notable for
        Chinese and Arabic. However it's worth noting that even if I broke off Hong Kong and assigned it to Cantonese,
        it would still not be big enough to make the top 20 list. The same goes for Catalonia, and ex-Yugoslavia, and
        all the other Chinese/Arabic dialects.

        Special exceptions were made to manually assign Singapore to English, Indonesia to Indo-Malay, Malaysia to
        Indo-Malay, based upon community feedback of previous editions of this report. Here are some links to previous
        editions of this report, which were posted on Reddit: <a href="https://old.reddit.com/r/languagelearning/comments/rs241i/the_20_languages_that_produce_82_of_the_worlds/">2021 edition</a>
            , <a href="https://old.reddit.com/r/languagelearning/comments/9i72xd/the_20_languages_that_produce_86_of_the_worlds/">2018 edition</a>
            , <a href="https://old.reddit.com/r/languagelearning/comments/6h7frz/just_20_languages_produce_about_80_of_the_worlds/">
            2017 edition</a>


        <h3>Default Country-To-Language Assignments (for languages which include multiple countries):</h3>

<ol>
    <li>
        English
        <ol>
            <li>In: USA, UK, Canada, Australia, Ireland, New Zealand, Singapore, Jamaica, Bahamas, Trinidad and Tobago, Barbados, Grenada, Guyana, Antigua and Barbuda, Belize</li>
            <li>Out: Puerto Rico, Hong Kong, Philippines, South Africa, Nigeria, Ghana, Zimbabwe, Uganda, Zambia, Botswana, Namibia, Kenya, Sierra Leone, Liberia</li>
        </ol>
    </li>

    <li>
        Chinese
        <ol>
            <li>In: People’s Republic of China, Taiwan Province of China, Hong Kong SAR, Macau SAR</li>
            <li>Out: Singapore</li>
        </ol>
    </li>

    <li>
        Spanish
        <ol>
            <li>In: Mexico, Spain, Argentina, Colombia, Chile, Peru, Venezuela, Ecuador, Dominican Republic, Guatemala, Panama, Paraguay, Costa Rica, Bolivia, Uruguay, El Salvador, Honduras, Nicaragua, Puerto Rico</li>
            <li>Out: USA, Equatorial Guinea, Cuba (no data)</li>
        </ol>
    </li>

    <li>
        German
        <ol>
            <li>In: Germany, Austria, Switzerland</li>
            <li>Out: Belgium, Luxembourg</li>
        </ol>
    </li>

    <li>
        Arabic
        <ol>
            <li>In: Saudi Arabia, Egypt, Iraq, Algeria, Qatar, Kuwait, Morocco, Oman, Sudan, Lebanon, Jordan, Tunisia, Bahrain, Libya, Syria</li>
            <li>Out: Israel, UAE, Yemen, Somalia, Mauritania (no data), Palestine (no data)</li>
        </ol>
    </li>

    <li>
        Russian
        <ol>
            <li>In: Russian Federation, Belarus</li>
            <li>Out: Latvia, Estonia, Ukraine, Kazakhstan</li>
        </ol>
    </li>

    <li>
        Malay-Indonesian
        <ol>
            <li>In: Indonesia, Malaysia</li>
        </ol>
    </li>

    <li>
        Portuguese
        <ol>
            <li>In: Brazil, Portugal, Angola, Mozambique, Cabo Verde</li>
        </ol>
    </li>

    <li>
        French
        <ol>
            <li>In: France, Mauritius, Benin, Congo, Dem. Rep. of the, Congo, Republic of, Cameroon, Togo</li>
            <li>Out: Canada, Belgium, Switzerland, Gabon, Lebanon, Algeria, Luxembourg, Cote d'Ivoire (no data)</li>
        </ol>
    </li>

    <li>
        Italian
        <ol>
            <li>In: Italy</li>
            <li>Out: Libya, Somalia, Albania, Switzerland</li>
        </ol>
    </li>

    <li>
        Korean
        <ol>
            <li>In: Korea, Republic of</li>
            <li>Out: North Korea (no data)</li>
        </ol>
    </li>

    <li>
        Persian
        <ol>
            <li>In: Iran, Afghanistan</li>
        </ol>
    </li>

    <li>
       Dutch
        <ol>
            <li>In: Netherlands, Belgium, Suriname</li>
        </ol>
    </li>
</ol>

        </div>
    )
}

export default Methodology
