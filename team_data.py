team_list = ['Arizona Cardinals',
             'Atlanta Falcons',
             'Baltimore Ravens',
             'Buffalo Bills',
             'Carolina Panthers',
             'Cincinnati Bengals',
             'Cleveland Browns',
             'Dallas Cowboys',
             'Chicago Bears',
             'Denver Broncos',
             'Detroit Lions',
             'Green Bay Packers',
             'Houston Texans',
             'Indianapolis Colts',
             'Jacksonville Jaguars',
             'Kansas City Chiefs',
             'Los Angeles Rams',
             'Miami Dolphins',
             'Minnesota Vikings',
             'New England Patriots',
             'New Orleans Saints',
             'New York Giants',
             'New York Jets',
             'Oakland Raiders',
             'Philadelphia Eagles',
             'Pittsburgh Steelers',
             'Los Angeles Chargers',
             'San Francisco 49ers',
             'Seattle Seahawks',
             'Tampa Bay Buccaneers',
             'Tennessee Titans',
             'Washington Redskins']

team_colors = {
    'Arizona Cardinals': [
        [0.53, 0.0, 0.15], [0.0, 0.0, 0.0], [0.93, 0.68, 0.12], [0.61, 0.63, 0.64]
        ],
    'Atlanta Falcons': [
        [0.64, 0.05, 0.18], [0.0, 0.0, 0.0], [0.65, 0.68, 0.69]],
    'Baltimore Ravens': [
        [0.1, 0.1, 0.37], [0.0, 0.0, 0.0], [0.73, 0.58, 0.2], [0.84, 0.04, 0.04]],
    'Buffalo Bills': [
        [0.05, 0.18, 0.51], [0.84, 0.04, 0.04]],
    'Carolina Panthers': [
        [0.0, 0.52, 0.79], [0.0, 0.0, 0.0], [0.75, 0.75, 0.75]],
    'Cincinnati Bengals': [
        [0.0, 0.0, 0.0], [0.83, 0.18, 0.12]],
    'Cleveland Browns': [
        [0.83, 0.18, 0.12], [0.13, 0.08, 0.05], [0.61, 0.63, 0.64]],
    'Dallas Cowboys': [
        [0.0, 0.08, 0.2], [0.69, 0.72, 0.74], [0.73, 0.79, 0.83], [0.61, 0.63, 0.64]],
    'Chicago Bears': [
        [0.04, 0.09, 0.16], [0.78, 0.22, 0.01]],
    'Denver Broncos': [
        [0.0, 0.14, 0.3], [1.0, 0.32, 0.0]],
    'Detroit Lions': [
        [0.0, 0.31, 0.54], [0.69, 0.72, 0.74], [0.0, 0.0, 0.0]],
    'Green Bay Packers': [
        [0.11, 0.18, 0.15], [0.93, 0.68, 0.12]],
    'Houston Texans': [
        [0.0, 0.03, 0.11], [0.64, 0.05, 0.18]],
    'Indianapolis Colts': [
        [0.0, 0.2, 0.41], [0.61, 0.63, 0.64]],
    'Jacksonville Jaguars': [
        [0.0, 0.0, 0.0], [0.0, 0.4, 0.46], [0.62, 0.47, 0.17], [0.84, 0.64, 0.16]],
    'Kansas City Chiefs': [
        [0.89, 0.09, 0.22], [0.93, 0.68, 0.12], [0.0, 0.0, 0.0]],
    'Los Angeles Rams': [
        [0.0, 0.08, 0.2], [0.69, 0.57, 0.36]],
    'Miami Dolphins': [
        [0.0, 0.56, 0.59], [0.96, 0.51, 0.13], [0.0, 0.34, 0.47]],
    'Minnesota Vikings': [
        [0.31, 0.15, 0.51], [1.0, 0.78, 0.18], [0.91, 0.75, 0.61], [0.0, 0.0, 0.0]],
    'New England Patriots': [
        [0.0, 0.08, 0.2], [0.84, 0.04, 0.04], [0.69, 0.72, 0.74]],
    'New Orleans Saints': [
        [0.62, 0.54, 0.35], [0.0, 0.0, 0.0]],
    'New York Giants': [
        [0.0, 0.14, 0.32], [0.64, 0.05, 0.18], [0.61, 0.63, 0.64]],
    'New York Jets': [
        [0.11, 0.18, 0.15], [0.15, 0.15, 0.12], [0.0, 0.0, 0.0]],
    'Oakland Raiders': [
        [0.65, 0.68, 0.69], [0.0, 0.0, 0.0]],
    'Philadelphia Eagles': [
        [0.0, 0.19, 0.21], [0.75, 0.75, 0.75], [0.73, 0.79, 0.83], [0.0, 0.0, 0.0], [0.37, 0.38, 0.38]],
    'Pittsburgh Steelers': [
        [0.0, 0.0, 0.0], [0.93, 0.68, 0.12], [0.84, 0.04, 0.04], [0.0, 0.33, 0.61], [0.61, 0.63, 0.64]],
    'Los Angeles Chargers': [
        [0.0, 0.08, 0.2], [0.0, 0.5, 0.77], [0.93, 0.68, 0.12]],
    'San Francisco 49ers': [
        [0.67, 0.0, 0.0], [0.69, 0.57, 0.36], [0.0, 0.0, 0.0], [0.61, 0.63, 0.64]],
    'Seattle Seahawks': [
        [0.0, 0.08, 0.2], [0.41, 0.75, 0.16], [0.61, 0.63, 0.64]],
    'Tampa Bay Buccaneers': [
        [0.84, 0.04, 0.04], [0.2, 0.19, 0.17], [0.0, 0.0, 0.0], [1.0, 0.47, 0.0], [0.69, 0.73, 0.75]],
    'Tennessee Titans': [
        [0.0, 0.08, 0.2], [0.27, 0.58, 0.82], [0.84, 0.04, 0.04], [0.75, 0.75, 0.75]],
    'Washington Redskins': [
        [0.25, 0.06, 0.06], [0.93, 0.68, 0.12], [0.0, 0.0, 0.0], [0.36, 0.17, 0.18]],
    }

team_logos = {
    'Arizona Cardinals': 'arizona-cardinals.png',
    'Atlanta Falcons': 'atlanta-falcons.png',
    'Baltimore Ravens': 'baltimore-ravens.png',
    'Buffalo Bills': 'buffalo-bills.png',
    'Carolina Panthers': 'carolina-panthers.png',
    'Chicago Bears': 'chicago-bears.png',
    'Cincinnati Bengals': 'cincinnati-bengals.png',
    'Cleveland Browns': 'cleveland-browns.png',
    'Dallas Cowboys': 'dallas-cowboys.png',
    'Denver Broncos': 'denver-broncos.png',
    'Detroit Lions': 'detroit-lions.png',
    'Green Bay Packers': 'green-bay-packers.png',
    'Houston Texans': 'houston-texans.png',
    'Indianapolis Colts': 'indianapolis-colts.png',
    'Jacksonville Jaguars': 'jacksonville-jaguars.png',
    'Kansas City Chiefs': 'kansas-city-chiefs.png',
    'Los Angeles Chargers': 'los-angeles-chargers.png',
    'Los Angeles Rams': 'los-angeles-rams.png',
    'Miami Dolphins': 'miami-dolphins.png',
    'Minnesota Vikings': 'minnesota-vikings.png',
    'New England Patriots': 'new-england-patriots.png',
    'New Orleans Saints': 'new-orleans-saints.png',
    'New York Giants': 'new-york-giants.png',
    'New York Jets': 'new-york-jets.png',
    'Oakland Raiders': 'oakland-raiders.png',
    'Philadelphia Eagles': 'philadelphia-eagles.png',
    'Pittsburgh Steelers': 'pittsburgh-steelers.png',
    'San Francisco 49ers': 'san-francisco-49ers.png',
    'Seattle Seahawks': 'seattle-seahawks.png',
    'Tampa Bay Buccaneers': 'tampa-bay-buccaneers.png',
    'Tennessee Titans': 'tennessee-titans.png',
    'Washington Redskins': 'washington-redskins.png',
    }