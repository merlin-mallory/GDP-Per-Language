import React, { useState, useEffect } from "react"
import './App.css';
import HeaderTitle from './components/HeaderTitle'
import HeaderLogin from "./components/HeaderLogin.jsx";
import BodyReport from "./components/BodyReport.jsx";
import FooterLeft from "./components/FooterLeft.jsx";
import FooterRight from "./components/FooterRight.jsx";

const App = () => {
    const [currentPage, setCurrentPage] = useState('report')

    return (
    <div className="App">
        <div className="HeaderContainer">
            <HeaderTitle />
            <HeaderLogin />
        </div>
        <div className="BodyContainer">
            <BodyReport currentPage={currentPage}/>
        </div>
        <div className="FooterContainer">
            <FooterLeft />
            <FooterRight setCurrentPage={setCurrentPage}/>
        </div>
    </div>
  )
}

export default App