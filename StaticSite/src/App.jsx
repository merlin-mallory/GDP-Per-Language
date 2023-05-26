import './App.css';
import HeaderTitle from './components/HeaderTitle'
import HeaderLogin from "./components/HeaderLogin.jsx";
import BodyReport from "./components/BodyReport.jsx";
import FooterLeft from "./components/FooterLeft.jsx";
import FooterRight from "./components/FooterRight.jsx";

const App = () => {

  return (
    <div className="App">
        <div className="HeaderContainer">
            <HeaderTitle />
            <HeaderLogin />
        </div>
        <BodyReport />
        <div className="FooterContainer">
            <FooterLeft />
            <FooterRight />
        </div>
    </div>
  )
}

export default App