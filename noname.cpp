///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxGridBagSizer* gbSizer1;
	gbSizer1 = new wxGridBagSizer( 0, 0 );
	gbSizer1->SetFlexibleDirection( wxBOTH );
	gbSizer1->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );

	m_textCtrl1 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( m_textCtrl1, wxGBPosition( 1, 0 ), wxGBSpan( 1, 4 ), wxALL|wxEXPAND, 5 );

	CE = new wxButton( this, wxID_ANY, wxT("CE"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( CE, wxGBPosition( 2, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );

	C = new wxButton( this, wxID_ANY, wxT("C"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( C, wxGBPosition( 2, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );

	/ = new wxButton( this, wxID_ANY, wxT("/"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( /, wxGBPosition( 2, 3 ), wxGBSpan( 1, 1 ), wxALL, 5 );

	1 = new wxButton( this, wxID_ANY, wxT("1"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 1, wxGBPosition( 3, 0 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	2 = new wxButton( this, wxID_ANY, wxT("2"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 2, wxGBPosition( 3, 1 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	3 = new wxButton( this, wxID_ANY, wxT("3"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 3, wxGBPosition( 3, 2 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	+ = new wxButton( this, wxID_ANY, wxT("+"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( +, wxGBPosition( 3, 3 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	4 = new wxButton( this, wxID_ANY, wxT("4"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 4, wxGBPosition( 4, 0 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	5 = new wxButton( this, wxID_ANY, wxT("5"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 5, wxGBPosition( 4, 1 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	6 = new wxButton( this, wxID_ANY, wxT("6"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 6, wxGBPosition( 4, 2 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	- = new wxButton( this, wxID_ANY, wxT("-"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( -, wxGBPosition( 4, 3 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	7 = new wxButton( this, wxID_ANY, wxT("7"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 7, wxGBPosition( 5, 0 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	8 = new wxButton( this, wxID_ANY, wxT("8"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 8, wxGBPosition( 5, 1 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	9 = new wxButton( this, wxID_ANY, wxT("9"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 9, wxGBPosition( 5, 2 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	* = new wxButton( this, wxID_ANY, wxT("*"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( *, wxGBPosition( 5, 3 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	= = new wxButton( this, wxID_ANY, wxT("="), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( =, wxGBPosition( 6, 3 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );

	0 = new wxButton( this, wxID_ANY, wxT("0"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( 0, wxGBPosition( 6, 0 ), wxGBSpan( 1, 2 ), wxALL|wxEXPAND, 5 );

	. = new wxButton( this, wxID_ANY, wxT("."), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( ., wxGBPosition( 6, 2 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );


	this->SetSizer( gbSizer1 );
	this->Layout();
	gbSizer1->Fit( this );

	this->Centre( wxBOTH );

	// Connect Events
	1->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::input_1 ), NULL, this );
}

MyFrame1::~MyFrame1()
{
	// Disconnect Events
	1->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::input_1 ), NULL, this );

}
