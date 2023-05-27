import React from "react"
import Methodology from "./Methodology"

const BodyReport = ({ currentPage }) => {
    return(
        <div className="BodyReport">
            {currentPage === 'report' ? (
                <div style={{position: 'relative', width: '100%', height: '0', paddingBottom: '56.25%'}}>
                    <iframe title="GDP_Per_Language2"
                        style={{position: 'absolute', top: '0', left: '0', width: '100%', height: '100%'}}
                        src="https://app.powerbi.com/reportEmbed?reportId=a18c1fa5-3898-4316-a5d9-595b5153bdb7&autoAuth=true&ctid=ce6d05e1-3c5e-4d62-87a8-4c4a2713c113"
                        frameBorder="0" allowFullScreen="true">
                    </iframe>
                </div>
            ) : (
                    <Methodology />
                )}
        </div>
    )
}


export default BodyReport