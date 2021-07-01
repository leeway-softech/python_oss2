from flask import Flask

import xlrd

import json

app = Flask(__name__)


def findCell(sh, searchedValue1):

    if searchedValue1 == "TOTAL SALARIES AND ALLOWANCES":
        for row in range(sh.nrows):
            for col in range(sh.ncols):
                myCell = sh.cell(row, col)
                if myCell.value == searchedValue1:
                    return sh.cell(row, col + 3)
    else:
        for row in range(sh.nrows):
            for col in range(sh.ncols):
                myCell = sh.cell(row, col)
                if myCell.value == searchedValue1:
                    return sh.cell(row, col + 1)

            # return xl_rowcol_to_cell(row, col+1)
    return -1


@app.route('/oss2')
def hello_world():
    headers = {'Access-Control-Allow-Origin': '*'}
    searchedValue = 'LOAN INTEREST A/C'
    searchedValue1 = 'GOLD LOAN INTEREST A/C'
    searchedValue2 = 'OD/LNFDR INTEREST A/C'
    searchedValue3 = 'CASH CREDIT /ODM'
    searchedValue4 = 'Accrued interest on Standard advances'
    searchedValue5 = 'Interest on market lending'
    searchedValue6 = 'ACCRUED INTR ON OUR'
    searchedValue7 = 'ACCRUED INTR ON GOVT'
    searchedValue8 = 'OUR INVESTMENTS INTEREST'
    searchedValue9 = 'INTEREST RECD. ON GOVT.'
    searchedValue10 = 'INTEREST RECD. ON'
    searchedValue11 = 'COMMISSION AND EXCHANGE'
    searchedValue12 = ' Profit (+) / Loss (-) on forex operations'
    searchedValue13 = ' Profit (+) / Loss (-) on trading and sale of securities'
    searchedValue14 = 'Dividend Income'
    searchedValue15 = 'ADMISSION FEES A/C'
    searchedValue16 = 'CHEQUE BOOK CHRGES'
    searchedValue17 = 'LOCKERS RENT'
    searchedValue18 = 'MISCELLENEOUS INCOME'
    searchedValue19 = 'INCOME FROM GOVT.'

    searchedValue20 = 'Profit / (Loss) on sale of fixed assets'
    searchedValue21 = 'Profit / (Loss) on sale of other assets '
    searchedValue22 = 'Other Non-operating Income '

    searchedValue23 = 'FIXED DEP. INTEREST'
    searchedValue24 = 'RECURRING DEP. INTEREST'
    searchedValue25 = 'SAVING BANK INTEREST'
    searchedValue26 = 'INTEREST PAID ON'
    searchedValue27 = 'On Inter-bank deposits'
    searchedValue28 = 'Others'

    searchedValue29 = 'TOTAL SALARIES AND ALLOWANCES'
    searchedValue30 = 'Directors fees'
    searchedValue31 = 'AUDIT FEES PAID'

    searchedValue32 = 'RENT A/C'
    searchedValue33 = 'ELECTRIC EXPENSES'
    searchedValue34 = 'INSURANCE'
    searchedValue35 = 'Law charges'

    searchedValue36 = 'POSTAGE AND TELEGRAMS'
    searchedValue37 = 'TELEPHONE EXPENSES'
    searchedValue38 = 'STATIONARY AND PRINTING'
    searchedValue39 = 'ADVERTISEMENT A/C'
    searchedValue40 = 'Advertisement and publicity'
    searchedValue41 = 'DEPRECIATION ON'
    searchedValue42 = 'REPAIRS & MAINTANANCE'

    searchedValue43 = 'Value adjustment of Securities'

    searchedValue44 = 'Bad Debts written off'
    searchedValue45 = 'Other assets written off'
    searchedValue46 = 'Capitalised expenditure written off'

    searchedValue47 = 'BAD & DOUBTFUL DEBT'
    searchedValue48 = 'PREMIUM PAID ON'
    searchedValue49 = 'Other risk provision'
    searchedValue50 = 'Other provisions'

    searchedValue51 = 'Capital gain'
    searchedValue52 = 'Capital losses'

    searchedValue53 = 'ADVANCE INCOME TAX'
    searchedValue54 = 'Balance of previous year'

    searchedValue55 = 'TRAVELLING EXPENSES'
    searchedValue56 = 'LEGAL EXPENCES'
    searchedValue57 = 'LOCAL CONVEYANCE'
    searchedValue58 = 'GST CREDIT REVERSE'
    searchedValue59 = 'COMPUTER MAINTAINCE'
    searchedValue60 = 'PHOTOCOPY AND TYPING'
    searchedValue61 = 'OFFICE EXPENSES'
    searchedValue62 = 'MISC. EXPENSES'
    searchedValue63 = 'SUBSCRIPTION'
    searchedValue64 = 'AGM EXPENSES'
    searchedValue65 = 'BOOKS AND PERIODICALS'
    searchedValue66 = 'CONSULTANCE FEES'
    searchedValue67 = 'COMPUTER STATIONERY'
    searchedValue68 = 'TRINING EXP'
    searchedValue69 = 'SECURITY EXPENSES'
    searchedValue70 = 'CLEARING HOUSE MAINT.'







    for sh in xlrd.open_workbook('PL_31032021.xlsx').sheets():
        if findCell(sh, searchedValue) == -1:
            loan = 0;

        else:
            loan = str(findCell(sh, searchedValue).value).replace(',', '')
            loan = round(float(loan) / 1000);
        if findCell(sh, searchedValue1) == -1:
            gold = 0;

        else:
            gold = str(findCell(sh, searchedValue1).value).replace(',', '')
            gold = round(float(gold) / 1000);
        if findCell(sh, searchedValue2) == -1:
            odin = 0;

        else:
            odin = str(findCell(sh, searchedValue2).value).replace(',', '')
            odin = round(float(odin) / 1000);
        if findCell(sh, searchedValue3) == -1:
            cash = 0;

        else:
            cash = str(findCell(sh, searchedValue3).value).replace(',', '')
            cash = round(float(cash) / 1000);
        if findCell(sh, searchedValue4) == -1:
            Accruedinterest = 0;

        else:
            Accruedinterest = str(findCell(sh, searchedValue4).value).replace(',', '')
            Accruedinterest = round(float(Accruedinterest) / 1000);
        if findCell(sh, searchedValue5) == -1:
            interstonmarket = 0;

        else:
            interstonmarket = str(findCell(sh, searchedValue5).value).replace(',', '')
            interstonmarket = round(float(interstonmarket) / 1000);
        if findCell(sh, searchedValue6) == -1:
            interstour = 0;

        else:
            interstour = str(findCell(sh, searchedValue6).value).replace(',', '')
            interstour = round(float(interstour) / 1000);
        if findCell(sh, searchedValue7) == -1:
            interstgvnt = 0;

        else:
            interstgvnt = str(findCell(sh, searchedValue7).value).replace(',', '')
            interstgvnt = round(float(interstgvnt) / 1000);
        if findCell(sh, searchedValue8) == -1:
            ourinvestinterset = 0;

        else:
            ourinvestinterset = str(findCell(sh, searchedValue8).value).replace(',', '')
            ourinvestinterset = round(float(ourinvestinterset) / 1000);
        if findCell(sh, searchedValue9) == -1:
            interestrcdgvnt = 0;

        else:
            interestrcdgvnt = str(findCell(sh, searchedValue9).value).replace(',', '')
            interestrcdgvnt = round(float(interestrcdgvnt) / 1000);
        if findCell(sh, searchedValue10) == -1:
            interstrcd = 0;

        else:
            interstrcd = str(findCell(sh, searchedValue10).value).replace(',', '')
            interstrcd = round(float(interstrcd) / 1000);
        if findCell(sh, searchedValue11) == -1:
            feecommi = 0;

        else:
            feecommi = str(findCell(sh, searchedValue11).value).replace(',', '')
            feecommi = round(float(feecommi) / 1000)+1;
        if findCell(sh, searchedValue12) == -1:
            profitlossforex = 0;

        else:
            profitlossforex = str(findCell(sh, searchedValue12).value).replace(',', '')
            profitlossforex = round(float(profitlossforex) / 1000);
        if findCell(sh, searchedValue13) == -1:
            profitlosstrading = 0;

        else:
            profitlosstrading = str(findCell(sh, searchedValue13).value).replace(',', '')
            profitlosstrading = round(float(profitlosstrading) / 1000);
        if findCell(sh, searchedValue14) == -1:
            dividentfund = 0;

        else:
            dividentfund = str(findCell(sh, searchedValue14).value).replace(',', '')
            dividentfund = round(float(dividentfund) / 1000);
        if findCell(sh, searchedValue15) == -1:
            adminfee = 0;

        else:
            adminfee = str(findCell(sh, searchedValue15).value).replace(',', '')
            adminfee = round(float(adminfee) / 1000);

        if findCell(sh, searchedValue16) == -1:
            cheque = 0;

        else:
            cheque = str(findCell(sh, searchedValue16).value).replace(',', '')
            cheque = round(float(cheque) / 1000);

        if findCell(sh, searchedValue17) == -1:
            lockers = 0;

        else:
            lockers = str(findCell(sh, searchedValue17).value).replace(',', '')
            lockers = round(float(lockers) / 1000);
        if findCell(sh, searchedValue18) == -1:
            missc = 0;

        else:
            missc = str(findCell(sh, searchedValue18).value).replace(',', '')
            missc = round(float(missc) / 1000);
        if findCell(sh, searchedValue19) == -1:
            income = 0;

        else:
            income = str(findCell(sh, searchedValue19).value).replace(',', '')
            income = round(float(income) / 1000);
        if findCell(sh, searchedValue20) == -1:
            profitfixed = 0;

        else:
            profitfixed = str(findCell(sh, searchedValue20).value).replace(',', '')
            profitfixed = round(float(profitfixed) / 1000);

        if findCell(sh, searchedValue21) == -1:
            profitother = 0;

        else:
            profitother = str(findCell(sh, searchedValue21).value).replace(',', '')
            profitother = round(float(profitother) / 1000);
        if findCell(sh, searchedValue22) == -1:
            othernon = 0;

        else:
            othernon = str(findCell(sh, searchedValue22).value).replace(',', '')
            othernon = round(float(othernon) / 1000)
        if findCell(sh, searchedValue23) == -1:
            fixeddepo = 0;

        else:
            fixeddepo = str(findCell(sh, searchedValue23).value).replace(',', '')
            fixeddepo = round(float(fixeddepo) / 1000);
        if findCell(sh, searchedValue24) == -1:
            recdepo = 0;

        else:
            recdepo = str(findCell(sh, searchedValue24).value).replace(',', '')
            recdepo = round(float(recdepo) / 1000);
        if findCell(sh, searchedValue25) == -1:
            savingdepo = 0;

        else:
            savingdepo = str(findCell(sh, searchedValue25).value).replace(',', '')
            savingdepo = round(float(savingdepo) / 1000);
        if findCell(sh, searchedValue26) == -1:
            paidonborrow = 0;

        else:
            paidonborrow = str(findCell(sh, searchedValue26).value).replace(',', '')
            paidonborrow = round(float(paidonborrow) / 1000);
        if findCell(sh, searchedValue27) == -1:
            interbank = 0;

        else:
            interbank = str(findCell(sh, searchedValue27).value).replace(',', '')
            interbank = round(float(interbank) / 1000);
        if findCell(sh, searchedValue28) == -1:
            other = 0;

        else:
            other = str(findCell(sh, searchedValue28).value).replace(',', '')
            other = round(float(other) / 1000);
        if findCell(sh, searchedValue29) == -1:
            staffexpense = 0;

        else:
            staffexpense = str(findCell(sh, searchedValue29).value).replace(',', '')
            staffexpense = round(float(staffexpense) / 1000);
            print(staffexpense);

        if findCell(sh, searchedValue30) == -1:
            director = 0;

        else:
            director = str(findCell(sh, searchedValue30).value).replace(',', '')
            director = round(float(director) / 1000);
        if findCell(sh, searchedValue31) == -1:
            auditorfee = 0;

        else:
            auditorfee = str(findCell(sh, searchedValue31).value).replace(',', '')
            auditorfee = round(float(auditorfee) / 1000);
        if findCell(sh, searchedValue32) == -1:
            rent = 0;

        else:
            rent = str(findCell(sh, searchedValue32).value).replace(',', '')
            rent = round(float(rent) / 1000);
        if findCell(sh, searchedValue33) == -1:
            electric = 0;

        else:
            electric = str(findCell(sh, searchedValue33).value).replace(',', '')
            electric = round(float(electric) / 1000);
        if findCell(sh, searchedValue34) == -1:
            insurance = 0;

        else:
            insurance = str(findCell(sh, searchedValue34).value).replace(',', '')
            insurance = round(float(insurance) / 1000);
        if findCell(sh, searchedValue35) == -1:
            lawcharge = 0;

        else:
            lawcharge = str(findCell(sh, searchedValue35).value).replace(',', '')
            lawcharge = round(float(lawcharge) / 1000);

        if findCell(sh, searchedValue36) == -1:
            postage = 0;

        else:
            postage = str(findCell(sh, searchedValue36).value).replace(',', '')
            postage = round(float(postage) / 1000);
        if findCell(sh, searchedValue37) == -1:
            telephone = 0;

        else:
            telephone = str(findCell(sh, searchedValue37).value).replace(',', '')
            telephone = round(float(telephone) / 1000);
        if findCell(sh, searchedValue38) == -1:
            stationary = 0;

        else:
            stationary = str(findCell(sh, searchedValue38).value).replace(',', '')
            stationary = float(stationary) / 1000;
        if findCell(sh, searchedValue39) == -1:
            adwertise = 0;

        else:
            adwertise = str(findCell(sh, searchedValue39).value).replace(',', '')
            adwertise =float(adwertise) / 1000;
        if findCell(sh, searchedValue40) == -1:
            adwertisepublicity = 0;

        else:
            adwertisepublicity = str(findCell(sh, searchedValue40).value).replace(',', '')
            adwertisepublicity = round(float(adwertisepublicity) / 1000);
        if findCell(sh, searchedValue41) == -1:
            deprecation = 0;

        else:
            deprecation = str(findCell(sh, searchedValue41).value).replace(',', '')
            deprecation = round(float(deprecation) / 1000);
        if findCell(sh, searchedValue42) == -1:
            repairandmaintance = 0;

        else:
            repairandmaintance = str(findCell(sh, searchedValue42).value).replace(',', '')
            repairandmaintance = round(float(repairandmaintance) / 1000);
        if findCell(sh, searchedValue43) == -1:
            valueadjustment = 0;

        else:
            valueadjustment = str(findCell(sh, searchedValue43).value).replace(',', '')
            valueadjustment = round(float(valueadjustment) / 1000);
        if findCell(sh, searchedValue44) == -1:
            baddebt = 0;

        else:
            baddebt = str(findCell(sh, searchedValue44).value).replace(',', '')
            baddebt = round(float(baddebt) / 1000);
        if findCell(sh, searchedValue45) == -1:
            otherassetswritten = 0;

        else:
            otherassetswritten = str(findCell(sh, searchedValue45).value).replace(',', '')
            otherassetswritten = round(float(otherassetswritten) / 1000);
        if findCell(sh, searchedValue46) == -1:
             Capitalisedexpenditur = 0;

        else:
            Capitalisedexpenditur = str(findCell(sh, searchedValue46).value).replace(',', '')
            Capitalisedexpenditur = round(float(Capitalisedexpenditur) / 1000);





        if findCell(sh, searchedValue47) == -1:
             provisionforloan = 0;

        else:
            provisionforloan = str(findCell(sh, searchedValue47).value).replace(',', '')
            provisionforloan = round(float(provisionforloan) / 1000);
        if findCell(sh, searchedValue48) == -1:
             provisionfordeprecision = 0;

        else:
            provisionfordeprecision = str(findCell(sh, searchedValue48).value).replace(',', '')
            provisionfordeprecision = round(float(provisionfordeprecision) / 1000);
        if findCell(sh, searchedValue49) == -1:
             otherriskprovisions = 0;

        else:
            otherriskprovisions = str(findCell(sh, searchedValue49).value).replace(',', '')
            otherriskprovisions = round(float(otherriskprovisions) / 1000);
        if findCell(sh, searchedValue50) == -1:
             otherprovisions = 0;

        else:
            otherprovisions = str(findCell(sh, searchedValue50).value).replace(',', '')
            otherprovisions = round(float(otherprovisions) / 1000);
        if findCell(sh, searchedValue51) == -1:
            nonoperatinggain = 0;

        else:
            nonoperatinggain = str(findCell(sh, searchedValue51).value).replace(',', '')
            nonoperatinggain = round(float(nonoperatinggain) / 1000);

        if findCell(sh, searchedValue52) == -1:
             nonoperatingloss = 0;

        else:
            nonoperatingloss = str(findCell(sh, searchedValue52).value).replace(',', '')
            nonoperatingloss = round(float(nonoperatingloss) / 1000);

        if findCell(sh, searchedValue53) == -1:
             provisiontax = 0;

        else:
            provisiontax = str(findCell(sh, searchedValue53).value).replace(',', '')
            provisiontax = round(float(provisiontax) / 1000);
        if findCell(sh, searchedValue54) == -1:
             balanceofprevyear = 0;

        else:
            balanceofprevyear = str(findCell(sh, searchedValue54).value).replace(',', '')
            balanceofprevyear = round(float(balanceofprevyear) / 1000);

   #expenses
        if findCell(sh, searchedValue55) == -1:
             travelexp = 0;

        else:
            travelexp = str(findCell(sh, searchedValue55).value).replace(',', '')
            travelexp = round(float(travelexp) / 1000);
        if findCell(sh, searchedValue56) == -1:
             legalexp = 0;

        else:
            legalexp = str(findCell(sh, searchedValue56).value).replace(',', '')
            legalexp = round(float(legalexp) / 1000);
        if findCell(sh, searchedValue57) == -1:
             conveyance = 0;

        else:
            conveyance = str(findCell(sh, searchedValue57).value).replace(',', '')
            conveyance = round(float(conveyance) / 1000);
        if findCell(sh, searchedValue58) == -1:
             gstcredit = 0;

        else:
            gstcredit = str(findCell(sh, searchedValue58).value).replace(',', '')
            gstcredit = round(float(gstcredit) / 1000);
        if findCell(sh, searchedValue59) == -1:
             computermaintain = 0;

        else:
            computermaintain = str(findCell(sh, searchedValue59).value).replace(',', '')
            computermaintain = round(float(computermaintain) / 1000);
        if findCell(sh, searchedValue60) == -1:
             photocopy = 0;

        else:
            photocopy = str(findCell(sh, searchedValue60).value).replace(',', '')
            photocopy = round(float(photocopy) / 1000);
        if findCell(sh, searchedValue61) == -1:
             officeexp = 0;

        else:
            officeexp = str(findCell(sh, searchedValue61).value).replace(',', '')
            officeexp = round(float(officeexp) / 1000);

        if findCell(sh, searchedValue62) == -1:
             miscexp = 0;

        else:
            miscexp = str(findCell(sh, searchedValue62).value).replace(',', '')
            miscexp = round(float(miscexp) / 1000);

        if findCell(sh, searchedValue63) == -1:
             subscription = 0;

        else:
            subscription = str(findCell(sh, searchedValue63).value).replace(',', '')
            subscription = round(float(subscription) / 1000);

        if findCell(sh, searchedValue64) == -1:
             agmexp = 0;

        else:
            agmexp = str(findCell(sh, searchedValue64).value).replace(',', '')
            agmexp = round(float(agmexp) / 1000);
        if findCell(sh, searchedValue65) == -1:
             bookperp = 0;

        else:
            bookperp = str(findCell(sh, searchedValue65).value).replace(',', '')
            bookperp = round(float(bookperp) / 1000)
        if findCell(sh, searchedValue66) == -1:
             consultance = 0;

        else:
            consultance = str(findCell(sh, searchedValue66).value).replace(',', '')
            consultance = round(float(consultance) / 1000);
        if findCell(sh, searchedValue67) == -1:
            computerst = 0;

        else:
            computerst = str(findCell(sh, searchedValue67).value).replace(',', '')
            computerst = round(float(computerst) / 1000);
        if findCell(sh, searchedValue68) == -1:
            traningexp = 0;

        else:
            traningexp = str(findCell(sh, searchedValue68).value).replace(',', '')
            traningexp = round(float(traningexp) / 1000);
        if findCell(sh, searchedValue69) == -1:
            securityexp3 = 0;

        else:
            securityexp3 = str(findCell(sh, searchedValue69).value).replace(',', '')
            securityexp3 = round(float(securityexp3) / 1000);
        if findCell(sh, searchedValue70) == -1:
            clghouse = 0;

        else:
            clghouse = str(findCell(sh, searchedValue70).value).replace(',', '')
            clghouse = round(float(clghouse) / 1000);



        actuallyreceived=loan+gold+odin+cash;
        Intersetreceivedfromotherbank=actuallyreceived+Accruedinterest;
        Interestonstandardinvestment=interstour+interstgvnt;
        interestonrbi=ourinvestinterset+interestrcdgvnt+interstrcd;
        Interestdiscountreceived=Intersetreceivedfromotherbank+interstonmarket+Interestonstandardinvestment+interestonrbi;
        misscell=adminfee+cheque+lockers+missc+income;
        otheroperatingincome=feecommi+profitlossforex+profitlosstrading+dividentfund+misscell;
        totaloperatingincome=Interestdiscountreceived+otheroperatingincome;
        nonoperatinfincome=profitfixed+profitother+othernon;
        totalincome=nonoperatinfincome+totaloperatingincome;
        customerdepo=fixeddepo+recdepo+savingdepo;
        Intersetpaid=customerdepo+paidonborrow+interbank+other;
        operatingexp=staffexpense+director+auditorfee;
        renttax=rent+electric;
        postagetelegrame=postage+telephone;
        print("STT==",stationary,"adwer===",adwertise);
        stationaryadvertise=round(adwertise+stationary);
        otheropexp=551;
        otheroperationgexpensetotal=renttax+insurance+lawcharge+postagetelegrame+stationaryadvertise+adwertisepublicity+deprecation+repairandmaintance+otheropexp;
        totaloperatingexpense=otheroperationgexpensetotal+operatingexp+Intersetpaid;
        totaloperatingprofitloss=totaloperatingincome-totaloperatingexpense;
        writeoff=valueadjustment+baddebt+otherassetswritten+Capitalisedexpenditur;
        provisionagainstriskcontigencies=provisionforloan+provisionfordeprecision+otherriskprovisions+otherprovisions;
        netoperatingprofitloss=totaloperatingprofitloss-valueadjustment-writeoff-provisionagainstriskcontigencies;
        netprofitbeforetax=netoperatingprofitloss+nonoperatinggain-nonoperatingloss;
        netprofitaftertax=netprofitbeforetax-provisiontax;
        netdistributableprofitloss=netprofitaftertax+balanceofprevyear;
        noninterestexpend=operatingexp+otheroperationgexpensetotal;
        TOTALOTHEROPERATINGEXPENSES=travelexp+legalexp+conveyance+gstcredit+computermaintain+photocopy+officeexp+miscexp+subscription+agmexp+bookperp+consultance+computerst+traningexp+securityexp3+clghouse;

        x1 = {

        "EARNING+++++++++++++++++++++++++++++++++++++++++++++++++++++": str("++++++++"),
        "Interest/discount received ":str(Interestdiscountreceived),
        "Interest/discount received on loans and advances":str(Intersetreceivedfromotherbank),
        "actuallyreceived": str(actuallyreceived),
        "Accrued interest on Standard advances":str(Accruedinterest),
        "Interest on market lending ":str(interstonmarket),
        "Interest on investments ":str(Interestonstandardinvestment),
        "Interest received /accrued on Standard Investment":str(Interestonstandardinvestment),
        "Interest on additional balance with RBI, inter-bank":str(interestonrbi),

        "Other Operating income":str(otheroperatingincome),
        "Fee, Commission, exchange and brokerage ":str(feecommi),
        "Profile loss on forex":str(profitlossforex),
        "profilt loss on trading":str(profitlosstrading),
        "Dividand income":str(dividentfund),
        "Miscellaneous Income":str(misscell),
        "Total Operating Income":str(totaloperatingincome),
        "Non Operating Income":str(nonoperatinfincome),
        "Profit / (Loss) on sale of fixed assets":str(profitfixed),
        "Profit / (Loss) on sale of other assets":str(profitother),
        "Other Non-operating Income":str(othernon),
        "Total income":str(totalincome),
        "Interest paid ":  str(Intersetpaid),
        "customerdeposit":  str(customerdepo),
        "On Inter-bank deposits":  str(interbank),
        "On Inter-bank borrowings":  str(paidonborrow),
        "Others":  str(other),

        "Operating Expenses":str(operatingexp),
        "Staff expenses":str(staffexpense),
        "Directors fees":str(director),
        "Auditor's fees":str(auditorfee),

        "Other Operating expenses":str(otheroperationgexpensetotal),
        "Rent, taxes and lighting ":str(renttax),
        "Insurance":str(insurance),
        "Law charges":str(lawcharge),
        "Postage, telegrams and stamps":str(postagetelegrame),
        "Stationery and printing":str(stationaryadvertise),
        "Advertisement and publicity":str(adwertisepublicity),
        "Depreciation on bank's property":str(deprecation),
        "Repairs and maintenance":str(repairandmaintance),
        "Others op":str(otheropexp),

        "Total operating expenses":str(totaloperatingexpense),

        "Total opratiing profit/loss":str(totaloperatingprofitloss),

        "Value adjustment of Securities":str(valueadjustment),

        "Write off":str(writeoff),
        "Bad Debts written off":str(baddebt),
        "Other assets written off":str(otherassetswritten),
        "Capitalised expenditure written off":str(Capitalisedexpenditur),

        "Provision against risks/ contingencies ":str(provisionagainstriskcontigencies),
        "Provision for loan losses":str(provisionforloan),
        "Provision for depreciation in investments including AFS":str(provisionfordeprecision),
        "Other risk provisions towards losses":str(otherriskprovisions),
        "Other provisions":str(otherprovisions),

        "Net Operating Profit (+)/Loss (-)":str(netoperatingprofitloss),

        "Non Operating Income gain":str(nonoperatinggain),

        "Non Operating Income losses":str(nonoperatingloss),

        "Net Profit Loss before taxes":str(netprofitbeforetax),
        "Provisions for taxes":str(provisiontax),
        "Net Profit Loss after taxes":str(netprofitaftertax),
        "Balance of previous years profit loss":str(balanceofprevyear),
        "Net distributable profit loss":str(netdistributableprofitloss),

        "Appropriation of profits":str(""),
        "Appropriation towards Statutory Reserves":str(""),
        "Appropriation towards Building Fund":str(""),
        "Appropriation towards Dividend Equalisation Fund":str(""),
        "Appropriation towards Other Reserves/ Provisions":str(""),
        "Dividend":str(""),

        "Net interest income":str(""),

        "Non-interest income":str(otheroperatingincome),

        "Non-interest expenditure":str(noninterestexpend),

        "Average Total Assets":str(""),
        "Average Earning Assets":str(""),
        "Working Fund":str(""),
        "Number of Employee":str(""),

        "INTEREST RECEIVABLE NOT RECOGNIZED":str("==============="),
        "Interest receivable not recognized during the quarter":str(""),
        "Balance at the beginning of the quarte":str(""),
        "Interest received and reversed to income from":str(""),
        "Balance at the end of the quarter":str(""),

        "DETAILS OF OTHER OPERATING EXPENSES==============================":str("============"),
        "TRAVELING EXP":str(travelexp),
        "LEGAL EXPENSES":str(legalexp),
        "CONVEYANCE EXP":str(conveyance),
        "GST CREDIT ENTRY REVERSED":str(gstcredit),
        "COMPUTER MAINTAINCE":str(computermaintain),
        "PHOTOCOPY":str(photocopy),
        "OFFICE EXP":str(officeexp),
        "MISC EXP ":str(miscexp),
        "SUBSCRIPTION":str(subscription),
        "AGM EXP":str(agmexp),
        "BOOKS AND PERIODICALS":str(bookperp),
        "CONSULTANCE FEES":str(consultance),
        "COMPUTER STATIONERY":str(computerst),
        "TRINING EXP":str(traningexp),
        "SECURITY EXPENSES":str(securityexp3),
        "CLG HOUSE MAIN CHRG":str(clghouse),
        "total":str(TOTALOTHEROPERATINGEXPENSES),









         }

        print(json.dumps(x1))
        return json.dumps(x1), headers
        input('Press ENTER to exit')


if __name__ == '__main__':
    app.run()
