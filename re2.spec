%define major 11
%define libname %mklibname re2
%define oldlibname %mklibname re2_ %{major}
%define develname %mklibname re2 -d
%define oddver %(echo %{version} |sed -e 's,\\.,-,g')
# (tpg) optimize it a bit
%global optflags %{optflags} -O3

Summary:	An efficient, principled regular expression library
Name:		re2
Version:	2024.02.01
Release:	1
License:	BSD like
Group:		System/Libraries
URL:		https://github.com/google/re2/releases
Source0:	https://github.com/google/re2/archive/%{oddver}/%{name}-%{oddver}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(absl)
BuildRequires:	pkgconfig(icu-uc)

%description
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python.

%package -n %{libname}
Summary:	An efficient, principled regular expression library
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python.

%package -n %{develname}
Summary:	Development files for the re2 library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python.

This package contains the development files for re2.

%prep
%autosetup -n re2-%{oddver} -p1

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DRE2_USE_ICU=ON \
    -G Ninja

%ninja_build

%install
%ninja_install -C build
rm -f %{buildroot}%{_libdir}/*.a

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc LICENSE
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
