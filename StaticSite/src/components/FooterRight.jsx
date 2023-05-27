import React from "react"

const FooterRight = ( {setCurrentPage } ) => {
    return(
        <div className="FooterRight">
            <a onClick={() => setCurrentPage('report')} href="#">Report</a> | <a
            onClick={() => setCurrentPage('methodology')} href="#">Methodology</a> | <a
            href="mailto:gdpperlang@gmail.com">Feedback</a>
        </div>
    )
}

export default FooterRight